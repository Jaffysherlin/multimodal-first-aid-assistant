from transformers import pipeline

# GPT-2 text generation
generator = pipeline('text-generation', model='gpt2')

def generate_guidance(injury_type, symptoms):
    prompt = f"Injury Type: {injury_type}\nSymptoms: {symptoms}\nProvide detailed first aid guidance:"
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text']
