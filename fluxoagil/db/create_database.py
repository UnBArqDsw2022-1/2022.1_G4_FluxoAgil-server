from fluxoagil.db.connection import Base, engine

# Se remover esses imports, as tabelas não são criadas.
from fluxoagil.models import Graduation, Curriculum

def create_database():
    Base.metadata.create_all(engine)
    print('>>> database created')

create_database()
