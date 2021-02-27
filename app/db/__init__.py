import databases
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core.config.database import DB

engine = create_engine(DB.to_string(), convert_unicode=True, pool_size=100, pool_pre_ping=True, pool_recycle=280)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
database= databases.Database(DB.to_string())
# migrate = Migrate()


