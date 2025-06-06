# Docker
Estudos de Docker para a criação de aplicações em containers 

configuração do .env
```
POSTGRES_USER=datauser # usuário 
POSTGRES_PASSWORD=123456789 # Senha do banco
POSTGRES_DB=meubanco # Nome do banco
POSTGRES_PORT=5432 # Porta
```

### Estrutura de diretórios
```
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py               # Entry point of the application
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py         # Configuration settings (e.g., environment variables)
│   │   ├── security.py       # Security utilities (e.g., JWT, OAuth2)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py           # Database models (e.g., SQLAlchemy or Pydantic models)
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py           # Pydantic schemas for request/response validation
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py           # Dependency injection utilities
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── user.py       # API routes for user-related endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py   # Business logic and service layer
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py           # Database connection and base models
│   │   ├── session.py        # Database session management
│   ├── tests/
│       ├── __init__.py
│       ├── test_user.py      # Unit and integration tests
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
├── alembic/                  # Database migrations (if using Alembic)
│   ├── env.py
│   ├── versions/
```

#### Requisitos linux

> Python
```
# Pacotes essenciais para Python
Esses pacotes são úteis para compilar e instalar dependências Python como psycopg2-binary, uvicorn, etc
sudo apt update
sudo apt install -y python3 python3-pip python3-venv build-essential

sudo apt install -y libpq-dev # Pacotes para uso com PostgreSQL. Necessário para compilar pacotes que dependem da libpq, como psycopg2.

# Recomendado (para segurança e criptografia)
# Utilizado por bibliotecas como python-jose, cryptography, bcrypt.
sudo apt install -y libssl-dev libffi-dev

```

> Docker
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Rodando a imagem Docker
```
# rodando a imagem
docker-compose up -d

# parando a imagem
docker-compose down
# ou 
docker stop <CONTAINER ID>

# rodar o postgres no terminal
docker-compose exec <db_name> psql -U <user>

# verificando os containers
docker ps -a
```

<a href="./app/README.md">documentação da API</a>
<a href="./esp32/README.md">documentação do Esp32</a>