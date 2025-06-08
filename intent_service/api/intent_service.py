import uuid

from fastapi import Request, BackgroundTasks


def init_analyze_intent(app):
    @app.post("/analyze_intent")
    async def analyze_intent(request: Request, background_tasks: BackgroundTasks):
        data = await request.json()
        unique_id = str(uuid.uuid4())
        background_tasks.add_task(app.analyze_chat.analyze, data, unique_id)

        return unique_id
