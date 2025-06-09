from InquirerPy import prompt, inquirer
import emoji
import os
from time import sleep
from config import frameworks, horas, estudo, nivel

def perguntar_framework(nome):
    print(emoji.emojize(f"{nome}, vamos falar sobre frameworks :snake:", language='pt'))
    pergunta = [
        {
            'type': "list",
            'message': emoji.emojize(f"{nome}, você usa algum framework? ↓ - ↑", language='pt'),
            'choices': frameworks,
            'name': 'framework'
        }
    ]
    resposta = prompt(pergunta)

    if resposta['framework'] == "Cancelar":
        print("Tudo bem! Nenhum framework selecionado.")
        return
    elif resposta['framework'] == "Outro?":
        outro = inquirer.text(message="Qual outro framework você usa?").execute()
        print(f"Legal! Você usa {outro}.")
    else:
        print(f"Muito bom! Você está usando {resposta['framework']}.")

def obter_metodo_estudo(nome):
    questoes = [
        {
            'type': "list", 
            'message': emoji.emojize(f'{nome}, por onde você estuda Python? :snake:', language='pt'),
            'choices': estudo,
            'name': 'metodo'
        }
    ]
    return prompt(questoes)

def obter_tempo_estudo(nome):
    tempo = [
        {
            'type': 'list',
            'message': f"{nome}, qual é o seu tempo de estudo por dia? (em horas) ↓ - ↑",
            'choices': horas,
            'name': 'esforço'
        }
    ]
    return prompt(tempo)

def avaliar_tempo_estudo(tempo_gasto):
    if tempo_gasto['esforço'] == '0-30 Min':
        print('Você está começando bem, mas tente aumentar o tempo gradualmente.')
    elif tempo_gasto['esforço'] == '1-2 Horas':
        print('Ótimo tempo!')
    elif tempo_gasto['esforço'] == '3-4 Horas':
        print('Bom tempo, isso trará bons resultados.')
    else:
        outros = inquirer.text(message='Quantas horas?').execute()
        print(f'{outros} horas! Muito bom!')

def perguntar_tempo(nome):
    perguntas = [
        {
            'type': "list", 
            'message': emoji.emojize(f"{nome}, qual é seu conhecimento em Python :snake:? ↓ - ↑", language='pt'),
            'choices': nivel,
            'name': 'conhecimento'
        }
    ]

    resultado = prompt(perguntas)
    os.system('cls' if os.name == 'nt' else 'clear')

    if resultado['conhecimento'] == "Cancelar":
        print(f"{nome}, você não escolheu uma opção válida.\nFechando programa!")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Programa encerrado!")
        return

    elif resultado['conhecimento'] == "Iniciante":
        print(f"{nome}, você é iniciante em Python. Continue estudando e praticando!")
        print("Recomendo começar com os fundamentos e praticar exercícios básicos.")

    elif resultado['conhecimento'] == "Intermediário":
        print(f"{nome}, você está no caminho certo. Continue praticando e aprendendo!")

    elif resultado['conhecimento'] == "Avançado":
        print(f"{nome}, você é avançado em Python. Continue se desafiando!")
        perguntar_framework(nome)

    metodo_resultado = obter_metodo_estudo(nome)
    if metodo_resultado['metodo'] == "Outro?":
        alternativa = input(f"{nome}, qual é o método que você usa para aprender Python?\n")
        print(f"Você estuda Python por meio de: {alternativa}. Que bacana!")

    tempo_gasto = obter_tempo_estudo(nome)
    avaliar_tempo_estudo(tempo_gasto)
