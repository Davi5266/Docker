import os

diretorios = [diretorio for diretorio in os.listdir('.') if os.path.isdir(os.path.join('.', diretorio))]
print(diretorios)
