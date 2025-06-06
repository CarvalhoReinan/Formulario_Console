from InquirerPy import prompt
import emoji

def obter_metodo_estudo(nome):
    questoes = [
        {
            'type': "list", 
            'message': (emoji.emojize(f'{nome}, Por onde você estuda Python? :cobra:', language='pt')),
            'choices': ["Youtube", "Google", "Livro", "Outro?"],
            'name': 'metodo'
        }
    ]
    return prompt(questoes)

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

def avaliar_tempo_estudo(tempo_gasto):
    if tempo_gasto['esforço'] == '0-30 Min':
        print('Você está no caminho certo, mas precisa de mais tempo para aprender.')
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
            'message': (emoji.emojize(f"{nome}, qual é seu conhecimento em Python :cobra:? ↓ - ↑ \n", language='pt')),
            'choices': ["Iniciante", "Intermediário", "Avançado", "Cancelar"],
            'name': 'conhecimento'
        }     
    ]
    
    resultado = prompt(perguntas)

    if resultado['conhecimento'] == "Cancelar":
        print("Você não escolheu uma opção válida")
        return

    metodo_resultado = obter_metodo_estudo(nome)
    if metodo_resultado['metodo'] == "Outro?":
        alternativa = input(f"{nome}, qual é o método que você usa para aprender Python? \n")
        print(f"Você estuda Python por meio de: {alternativa} !")

    tempo_gasto = obter_tempo_estudo(nome)
    avaliar_tempo_estudo(tempo_gasto)

def main():
    nome = input("Qual é o seu nome? ")
    perguntar_tempo(nome)

if __name__ == "__main__":
    main()
