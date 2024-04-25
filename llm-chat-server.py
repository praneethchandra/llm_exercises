import os
import json
import glob
from langchain_community.llms import LlamaCpp, GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from flask import Flask, jsonify, request

llm_to_use = "llama" # llama or gpt4all

llm = None

if llm_to_use == "llama":
    n_gpu_layers = 1 # Metal set to 1 is enough.
    n_batch = 512 # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.

    #Make sure the model path is correct for your system
    llm = LlamaCpp(
        model_path="./models/llama.gguf",
        n_gpu_layers=n_gpu_layers,
        n_batch=n_batch,
        n_ctx=2048,
        f16_kv=True, # MUST set to True, otherwise you will run into problem after a couple of calls
        verbose=True
    )
else:
    local_path = (
        "./models/gpt4.gguf"
    )
    # Callbacks support token-wise streaming
    callbacks = (StreamingStdOutCallbackHandler())

    llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)
    llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)


app = Flask(__name__)

@app.route('/chat', method=['POST'])
def chat():
    message = request.get_data(as_text=True)
    
    if llm is not None:
        output = llm.invoke(message)
        print(output)
        return output

    return "Internal Server Error"