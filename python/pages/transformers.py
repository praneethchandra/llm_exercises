from transformers import pipeline


classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")

classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)


classifier = pipeline("zero-shot-classification")
classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

classifier = pipeline("text-generation")
classifier("In this course, we will teach you how to")

classifier = pipeline("translation_en_to_fr")






