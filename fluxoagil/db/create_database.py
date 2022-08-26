from fluxoagil.db.connection import Base, engine
from fluxoagil.models import Graduation

def create_database():
    Base.metadata.create_all(engine)
    print('>>> database created')

create_database()