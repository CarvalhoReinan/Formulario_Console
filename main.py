from formulario_Console import perguntar_tempo
import emoji
import os

def boas_vindas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(emoji.emojize("👋 Olá! Bem-vindo ao seu assistente de estudos em Python 🐍", language='pt'))

def iniciar_programa():
    boas_vindas()
    nome = input("Qual é o seu nome? ")
    perguntar_tempo(nome)

if __name__ == "__main__":
    iniciar_programa()