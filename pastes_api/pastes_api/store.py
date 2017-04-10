from flask_mysqldb import MySQL

from .app import app

# Init DB
database = MySQL(app)

database_schema = """
    CREATE TABLE IF NOT EXISTS pastes (
        id INT NOT NULL AUTO_INCREMENT,
        content TEXT NOT NULL,
        created_at int NOT NULL,
        PRIMARY KEY (id)
    );
"""


# Commands
@app.cli.command('initdb')
def init_db():
    """Creates the database if not exists"""
    app.logger.debug("Initializing database")
    cursor = database.connection.cursor()
    # try:
    cursor.execute(database_schema)
    # database.commit()
    # except:
    #     database.rollback()
