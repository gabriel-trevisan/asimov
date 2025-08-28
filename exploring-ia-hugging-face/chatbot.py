from transformers import pipeline

chatbot = pipeline(task='text-generation', model='Felladrin/Llama-68M-Chat-v1', max_new_tokens=50)

pergunta = 'Hi, what is your name?'
resposta = chatbot(pergunta)

print(resposta)