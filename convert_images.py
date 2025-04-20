from PIL import Image, ImageDraw
import os

# Cria a pasta static se não existir
os.makedirs('static', exist_ok=True)

# Cria o favicon
favicon = Image.new('RGB', (32, 32), '#4CAF50')
draw = ImageDraw.Draw(favicon)
# Desenha o quadrado branco
draw.rectangle([2, 2, 30, 30], fill='white', outline='#4CAF50', width=2)
# Desenha o quadrado verde menor
draw.rectangle([8, 8, 24, 24], outline='#4CAF50', width=2)
# Desenha o quadrado verde central
draw.rectangle([12, 12, 20, 20], fill='#4CAF50')
favicon.save('static/favicon.png')

# Cria o logo
logo = Image.new('RGB', (200, 200), '#4CAF50')
draw = ImageDraw.Draw(logo)
# Desenha o quadrado branco
draw.rectangle([10, 10, 190, 190], fill='white', outline='#4CAF50', width=4)

# Desenha as linhas horizontais
draw.line([10, 70, 190, 70], fill='#4CAF50', width=4)
draw.line([10, 130, 190, 130], fill='#4CAF50', width=4)

# Desenha as linhas verticais
draw.line([70, 10, 70, 190], fill='#4CAF50', width=4)
draw.line([130, 10, 130, 190], fill='#4CAF50', width=4)

# Adiciona os números
from PIL import ImageFont
try:
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font = ImageFont.load_default()

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = [(30, 45), (100, 45), (170, 45),
             (30, 105), (100, 105), (170, 105),
             (30, 165), (100, 165), (170, 165)]

for num, pos in zip(numbers, positions):
    draw.text(pos, num, fill='#4CAF50', font=font, anchor='mm')

logo.save('static/logo.png') 