from fastapi import FastAPI

from src.test_task.router import router as test_task_router


class Application:
    def get_app(self) -> FastAPI:
        server: FastAPI = FastAPI()
        self._setup(server)
        return server

    def _setup(self, server: FastAPI):
        server.include_router(test_task_router)


app: FastAPI = Application().get_app()
