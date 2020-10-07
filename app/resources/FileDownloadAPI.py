import os

from fastapi import APIRouter
from fastapi.responses import FileResponse, StreamingResponse

router = APIRouter()
UPLOAD_FOLDER = "E:\sure-delete"


@router.get("/showImage/{filename}",
            tags=["Download or Show File"],
            description="Show the file or Image",
            summary="Show the file or Image",
            response_class=FileResponse,
            responses={
                400: {
                    "content": {"plain/text": {}},
                    "description": "Bad Request or Operation forbidden",
                },
                500: {
                    "content": {"plain/text": {}},
                    "description": "Internal Server Error.",
                }
            },
            )
def download(filename: str):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return FileResponse(path)


@router.get("/download/{filename}",
            tags=["Download or Show File"],
            description="Download a file by file name",
            summary="Download a file by file name",
            response_class=FileResponse,
            responses={
                400: {
                    "content": {"plain/text": {}},
                    "description": "Bad Request or Operation forbidden",
                },
                500: {
                    "content": {"plain/text": {}},
                    "description": "Internal Server Error.",
                }
            },
            )
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return FileResponse(path, filename=filename)


@router.get("/streamDownload/{filename}",
            tags=["Download or Show File"],
            description="Download a file by file name using FastAPI Stream Download",
            summary="Download a file by file name using FastAPI Stream Download",
            response_class=StreamingResponse,
            responses={
                400: {
                    "content": {"plain/text": {}},
                    "description": "Bad Request or Operation forbidden",
                },
                500: {
                    "content": {"plain/text": {}},
                    "description": "Internal Server Error.",
                }
            },
            )
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    file_like = open(path, mode="rb")
    response = StreamingResponse(file_like, media_type="application/octet-stream")
    response.status_code = 200
    response.headers["Content-Disposition"] = "attachment; filename=" + filename
    return response
