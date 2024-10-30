import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

def generate_youtube_script(prompt, max_length=300):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, no_repeat_ngram_size=2)
    return tokenizer.decode(output[0], skip_special_tokens=True)
