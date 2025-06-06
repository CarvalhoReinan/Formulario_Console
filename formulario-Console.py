from InquirerPy import prompt
import emoji
from time import sleep
import os
# Formulário de Console para avaliar o tempo de estudo em Python

def obter_metodo_estudo(nome):
    questoes = [
        {
            'type': "list", 
            'message': (emoji.emojize(f'{nome}, Por onde você estuda Python? :cobra:', language='pt')),
            'choices': ["Youtube", "Google", "Livro", "Outro?"],
            'name': 'metodo'
        }
    ]
    return prompt(questoes) #Pergunta sobre o método de estudo através do console onde o usuário escolhe uma opção e assim retorna o resultado

def obter_tempo_estudo(nome):
    tempo = [
        {
            'type': 'list',
            'message': f"{nome}, Qual é o seu tempo de estudo por dia? (em horas) ↓ - ↑\n",
            'choices': ['0-30 Min', '1-2 Horas', '3-4 Horas', 'Outro?'],
            'name': 'esforço'
        }
    ]
    return prompt(tempo)

def avaliar_tempo_estudo(tempo_gasto): # Avalia o tempo gasto pelo usuário
    if tempo_gasto['esforço'] == '0-30 Min':
        print('Você está começando bem, mas tente aumentar o tempo gradualmente.')
    elif tempo_gasto['esforço'] == '1-2 Horas':
        print('Ótimo tempo!')
    elif tempo_gasto['esforço'] == '3-4 Horas':
        print('Bom tempo, isso trará bons resultados.')
    else:
        outros = input('Quantas horas? ')
        print(f'{outros} horas ! Muito bom!')

def perguntar_tempo(nome):
    # Pergunta sobre o conhecimento em Python
    perguntas = [
        {
            'type': "list", 
            'message': (emoji.emojize(f"{nome}, qual é seu conhecimento em Python :cobra: ? ↓ - ↑ \n", language='pt')),
            'choices': ["Iniciante", "Intermediário", "Avançado", "Cancelar"],
            'name': 'conhecimento'
        }     
    ]
    
    resultado = prompt(perguntas)

    if resultado['conhecimento'] == "Cancelar":
        print(f"{nome}, Você não escolheu uma opção válida \n Fechando Programa !")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Programa encerrado !")
        
        return

    metodo_resultado = obter_metodo_estudo(nome)
    if metodo_resultado['metodo'] == "Outro?":
        alternativa = input(f"{nome}, qual é o método que você usa para aprender Python? \n")
        print(f"Você estuda Python por meio de: {alternativa}, que bacana !")

    tempo_gasto = obter_tempo_estudo(nome)
    avaliar_tempo_estudo(tempo_gasto)

def main():
    nome = input("Qual é o seu nome? ")
    perguntar_tempo(nome)

if __name__ == "__main__":
    main()
