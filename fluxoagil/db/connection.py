import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Na formatação dessa string existem um símbolos especiais. Para saber o porquê
# deles, dê uma olhada na documentação:
# https://docs.sqlalchemy.org/en/14/core/engines.html#engine-configuration
connection_string = 'postgresql+psycopg2://'
connection_string += f'{os.getenv("POSTGRES_USER")}'
connection_string += f':{os.getenv("POSTGRES_PASSWORD")}'
connection_string += f'@{os.getenv("POSTGRES_HOST")}'
connection_string += f':{os.getenv("POSTGRES_PORT")}'
connection_string += f'/{os.getenv("POSTGRES_DB")}'

engine = create_engine(connection_string, echo=True, future=True)
