import spacy
import en_core_web_sm
import streamlit as st
import spacy_streamlit 

models = ["en_core_web_sm"]
nlp = spacy.load("en_core_web_sm")
default_text = "Sundar Pichai is the CEO of the Google"
visualizers = ["ner", "textcat"]
# nlp = en_core_web_sm.load()

ref_response = st.text_area("Enter ref response", None)

if ref_response is not None:
    ref_entities = nlp(ref_response)
    st.write("Reference Entities")
    st.write([(w.text, w.pos_) for w in ref_entities])

llm_response = st.text_area("Enter llm response", None)    

if llm_response is not None:
    llm_entities = nlp(llm_response)
    st.write("Llm Entities")
    st.write([(w.text, w.pos_) for w in llm_entities])

spacy_streamlit.visualize(models, default_text, visualizers)