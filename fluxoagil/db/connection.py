
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:password@fluxoagil-db:5432/fluxoagil_db', echo=True, future=True)
