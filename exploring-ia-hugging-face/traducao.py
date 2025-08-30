from transformers import pipeline

modelo = 'facebook/mbart-large-50-many-to-many-mmt'

mensagem = 'Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.'

tradutor = pipeline(task='translation', model=modelo)

resposta = tradutor(mensagem, src_lang='pt_XX', tgt_lang='en_XX')

print(resposta[0]['translation_text'])

