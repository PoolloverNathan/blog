try:
    import sqlite3
except ModuleNotFoundError:
    import sqlite3d as sqlite3
db = sqlite3.connect("database.db")
db.executescript("schema.sql")
db.commit()
