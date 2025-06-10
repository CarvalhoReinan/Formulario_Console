# 📊 Estudo em Python - Console Form

Um formulário interativo no terminal feito com [InquirerPy](https://github.com/kazhala/InquirerPy) para ajudar desenvolvedores a refletirem sobre seus hábitos de estudo em Python 🐍.

## 🚀 Sobre o Projeto

Este projeto tem como objetivo criar um **questionário leve, divertido e personalizável** para usuários avaliarem:

- Seu nível atual em Python.
- Quanto tempo dedicam aos estudos.
- Por onde estão aprendendo.
- Se já usam algum framework back-end (como Flask ou Django).

## 🧰 Tecnologias e Bibliotecas

- Python 3.10+
- [InquirerPy](https://github.com/kazhala/InquirerPy)
- [emoji](https://github.com/carpedm20/emoji)

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
## 📦 Como Instalar

```bash
git clone https://github.com/CarvalhoReinan/formulario_console.git
cd formulario-console
pip install InquirerPy 
pip install emoji
```

## ▶️ Como Executar

No terminal, digite:

```bash
python formulario-Console.py
```

Você será guiado por um conjunto de perguntas que adaptam a conversa com base nas suas respostas.

## 📁 Estrutura do Projeto

```
.
├── config.py          # Dados fixos como listas de opções
├── perguntas.py       # Lógica das perguntas interativas
├── main.py            # Ponto de entrada
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

## ✍️ Personalização

Você pode facilmente:

- Adicionar novos frameworks em `config.py`.
- Alterar o estilo das mensagens.
- Incluir novas perguntas no arquivo `perguntas.py`.

## 📸 Preview (simulação)

```
Qual é o seu nome? Reii
Reii, qual é seu conhecimento em Python 🐍 ? ↓ - ↑
❯ Iniciante
  Intermediário
  Avançado
  Cancelar

Reii, você é iniciante em Python, continue estudando e praticando!
Por onde você estuda Python? 🐍
❯ Youtube
  Google
  Livro
  Outro?
```

## 📌 Status

🛠 Em desenvolvimento. Sinta-se livre para sugerir melhorias ou abrir issues!

## 💡 Melhorias Futuras (planejadas)

- Armazenar respostas em arquivos `.json` ou `.csv`
- Adicionar sistema de progresso ou pontuação
- Recomendação de conteúdos com base nas respostas

## 📄 Licença

Este projeto é livre para estudos e modificações.  
Se quiser contribuir ou deixar sugestões, sinta-se à vontade!

---

Feito com 💻 por [CarvalhoReinan](https://github.com/CarvalhoReinan)
