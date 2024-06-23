#!/usr/bin/python3
"""
script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()

    Base.metadata.create_all(engine)

    new_state = State(name='Louisiana')

    # Add and commit state to session
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
