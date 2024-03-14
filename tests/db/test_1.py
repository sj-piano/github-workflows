import os
from sqlalchemy import (
    create_engine,
    text,
)
from sqlalchemy.sql.ddl import CreateSchema
from sqlalchemy_utils import (
    database_exists,
    create_database,
    drop_database,
)


DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

TEST_DB_NAME = "test_db"


def test_foo():
    db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TEST_DB_NAME}"
    if database_exists(db_url):
        drop_database(db_url)
    create_database(db_url)
    engine = create_engine(db_url)
    assert database_exists(db_url) is True
    engine.execute(CreateSchema("test_schema"))
    engine.execute(text("CREATE TABLE test_schema.test_table (id serial PRIMARY KEY, name VARCHAR(50));"))
    engine.execute(text("INSERT INTO test_schema.test_table (name) VALUES ('test');"))
    result = engine.execute(text("SELECT * FROM test_schema.test_table;"))
    assert result.fetchone() == (1, "test")
    drop_database(db_url)
