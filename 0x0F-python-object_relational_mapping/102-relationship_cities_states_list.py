#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
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

    cities = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
