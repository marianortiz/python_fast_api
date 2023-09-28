from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import Connection as SQLite3Connection
from sqlalchemy.engine import Engine
from sqlalchemy import event

SQLALCHEMY_DATABASE_URL_LITE = "sqlite:///./app.db"

MYSQL_HOST = config('SQL_HOST')
MYSQL_USER = config('SQL_USER')
MYSQL_PASSWORD = config('SQL_PASS')
MYSQL_BD = config('SQL_DATABASE')
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_BD}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL_LITE,
                           connect_args={"check_same_thread": False})

    @event.listens_for(Engine, 'connect')
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            # 'PRAGMA foreign_keys = ON;'
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.close()
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
