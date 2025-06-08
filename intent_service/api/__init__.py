def initialize_api(app):
    from api.intent_service import init_analyze_intent
    init_analyze_intent(app)
