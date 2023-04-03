# pip install transformers
# pip3 install torch torchvision torchaudio

from transformers import pipeline
# model = pipeline("text-generation", model = "gpt2")

# sentence = model("Hi, My name is John Cena, I am here",
#                  do_sample=True, top_k=50,
#                  temperature=0.9, max_length=100,
#                  num_return_sentences=2)
#
# for i in sentence:
#   print(i["generated_text"])

text_generation = pipeline("text-generation", model = "gpt2")

prefix_text = "The world is"

generated_text= text_generation(prefix_text, max_length=50, do_sample=False)[0]

print(generated_text["generated_text"])

