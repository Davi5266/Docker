import socket

def my_address():
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)

	# Abra o arquivo em modo "w" (write) para criar ou sobrescrever.
	# Se o arquivo já existir, ele será sobrescrito.
	arquivo = open(".env", "w")

	# Escreva a string no arquivo
	arquivo.write("DB_IP=%s\n" % IPAddr)  # \n adiciona uma quebra de linha

	# Feche o arquivo
	arquivo.close()

	print("Arquivo criado e conteúdo escrito com sucesso!")

my_address()
