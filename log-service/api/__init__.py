def initialize_app(app):

    from api.log_service import init_log_service
    init_log_service(app)

    from api.log_service import init_get_service
    init_get_service(app)

    from api.database_service import init_create_database
    init_create_database(app)

