#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    search = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter(State.name == search).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
