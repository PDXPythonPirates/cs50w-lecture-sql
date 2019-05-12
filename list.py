import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

conn_args = {}
if 'pg8000' in os.getenv('DATABASE_URL'):
    conn_args = {'ssl': True}

engine = create_engine(os.getenv("DATABASE_URL"), connect_args=conn_args)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
