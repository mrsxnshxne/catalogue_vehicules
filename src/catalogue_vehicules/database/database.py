from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from catalogue_vehicules.routers.engine import create_engine

USER="root"
PASSWORD="root"
HOST="mariadb"
PORT="3306"
DB_NAME="catalogue_vehicules"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()