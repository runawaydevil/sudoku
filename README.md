# 🧩 Sudoku Web

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Um jogo de Sudoku desenvolvido em Python com Flask, oferecendo uma experiência de jogo intuitiva e responsiva.

## 🚀 Funcionalidades

- Interface web responsiva e moderna
- Três níveis de dificuldade (Fácil, Médio e Difícil)
- Validação de soluções em tempo real
- Botões de Reset e Novo Jogo
- Design limpo e intuitivo
- Favicon e logo personalizados

## 📋 Requisitos

- Python 3.6+
- Flask 2.0.1
- Werkzeug 2.0.1
- Jinja2 3.0.1
- itsdangerous 2.0.1
- click 8.0.1
- svglib 1.5.1
- reportlab 4.0.9

## 🛠️ Instalação

### Windows

1. Clone este repositório:
```bash
git clone https://github.com/runawaydevil/sudoku.git
cd sudoku-web
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Converta os arquivos SVG em PNG:
```bash
python convert_images.py
```

### Linux/Mac

1. Clone este repositório:
```bash
git clone https://github.com/runawaydevil/sudoku-web.git
cd sudoku-web
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Converta os arquivos SVG em PNG:
```bash
python convert_images.py
```

## 🎮 Como Jogar

1. Inicie o servidor:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:3698
```

3. Escolha a dificuldade:
   - Fácil: 30% das células preenchidas
   - Médio: 50% das células preenchidas
   - Difícil: 70% das células preenchidas

4. Controles:
   - Clique em uma célula vazia e digite um número (1-9)
   - Use Backspace ou Delete para apagar um número
   - Clique em "Reset" para reiniciar o jogo atual
   - Clique em "Novo Jogo" para começar um novo jogo
   - Clique em "Verificar" para verificar sua solução

## 📝 Regras do Sudoku

- Cada linha deve conter os números de 1 a 9 sem repetição
- Cada coluna deve conter os números de 1 a 9 sem repetição
- Cada quadrado 3x3 deve conter os números de 1 a 9 sem repetição

## 🏗️ Estrutura do Projeto

```
sudoku-web/
├── static/
│   ├── favicon.svg
│   ├── favicon.png
│   ├── logo.svg
│   └── logo.png
├── templates/
│   └── index.html
├── app.py
├── convert_images.py
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Lógica do Jogo: Algoritmo de Backtracking
- Design: SVG, CSS Moderno

## 👨‍💻 Desenvolvedor

Desenvolvido por [Pablo Murad (runawaydevil)](https://github.com/runawaydevil)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 