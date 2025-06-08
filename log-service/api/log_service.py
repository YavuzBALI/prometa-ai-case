from fastapi import Request, BackgroundTasks


def init_log_service(app):
    @app.post("/log")
    async def logging(request: Request, background_tasks: BackgroundTasks):
        data = await request.json()
        background_tasks.add_task(app.log_service.log, data)

        return {"message": "Logging Requests Successful"}

def init_get_service(app):
    @app.get("/get_log")
    async def get_log(unique_id: str):
        data = app.log_service.get_logs(unique_id)
        return data