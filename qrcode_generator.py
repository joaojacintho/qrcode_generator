# Importando a lib que gera o QRCode
import pyqrcode

# Passando o link que será vinculado ao código
url_for_generate = pyqrcode.create('https://www.google.com/')

# Dizendo qual será o tipo de saída
url_for_generate.svg('qrcode.svg', scale=8)
url_for_generate.png('qrcode.png', scale=10)


