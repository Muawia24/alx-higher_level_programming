#!/usr/bin/python3
"""
creates the State "California" with the City
"San Francisco" from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # create a state
    city = City(name='San Francisco')
    state = State(name='California')
    # Add a city to state
    state.cities = [city]

    session.add_all([state, city])
    session.commit()
    session.close()
