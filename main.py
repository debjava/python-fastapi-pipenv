from fastapi import FastAPI
import uvicorn

from app.resources import DeleteApi, PutAPI, PostAPI, PatchAPI, FileUploadAPI, FileDownloadAPI

CONTEXT_PATH = "/myapp"

app = FastAPI()

subapi = FastAPI(
                    title="My Demo Project using Python FastAPI",
                    description="This is an example project which uses Python FastAPI",
                    version="1.0.0",
                )

subapi.include_router(DeleteApi.router)
subapi.include_router(PutAPI.router)
subapi.include_router(PostAPI.router)
subapi.include_router(PatchAPI.router)
subapi.include_router(FileUploadAPI.router)
subapi.include_router(FileDownloadAPI.router)

# Mount the SubApi
app.mount(CONTEXT_PATH, subapi)


if __name__ == "__main__":
    print("Navigate the url: http://localhost:8090/myapp/docs for Swagger docs")
    uvicorn.run(app, host="0.0.0.0", port=8090)
