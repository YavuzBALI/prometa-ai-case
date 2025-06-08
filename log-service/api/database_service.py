from database.database_model import init_db

def init_create_database(app):
    @app.on_event("startup")
    async def create_database():
       init_db()
