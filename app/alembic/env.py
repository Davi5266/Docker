# app/alembic
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Adiciona o diretório `app` ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Importa Base e os modelos
from db.base import Base
from db.base_model_imports import *  # importa os modelos para o metadata

# configuração de conexão
config = context.config
fileConfig(config.config_file_name)

# Define o metadata usado para 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline():
    """Executa migrações sem conexão real (gera SQL)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()