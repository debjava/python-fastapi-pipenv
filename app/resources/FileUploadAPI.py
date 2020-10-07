import json
import os
import shutil
from types import SimpleNamespace
from typing import List

from fastapi import APIRouter, Response, File, UploadFile, Body, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse

from app.services import EmployeeServices as empService

router = APIRouter()
UPLOAD_FOLDER = "E:\sure-delete"


@router.post("/singleFile",
             tags=["Upload File"],
             description="Upload a file",
             summary="Upload a file",
             response_class=PlainTextResponse,
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
def uploadSingleFile(file: UploadFile = File(...)):
    fileName = file.filename
    print("Uploaded File Name: ", fileName)

    file_object = file.file
    upload_folder = open(os.path.join(UPLOAD_FOLDER, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()

    resText = "File with file name " + fileName + " uploaded successfully"
    return Response(content=resText, status_code=200, media_type="plain/text")


@router.post("/multipleFiles",
             tags=["Upload File"],
             description="Upload a list of files",
             summary="Upload a list of files",
             response_class=PlainTextResponse,
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
def uploadMultipleFiles(files: List[UploadFile] = File(...)):
    for file in files:
        file_object = file.file
        upload_folder = open(os.path.join(UPLOAD_FOLDER, file.filename), 'wb+')
        shutil.copyfileobj(file_object, upload_folder)
        upload_folder.close()
    return Response(content="All files uploaded successfully", status_code=200, media_type="plain/text")


@router.post("/uploadEmpProfile",
             tags=["Upload File"],
             description="Upload a file along with employee information in json format",
             summary="Upload a file along with employee information in json format",
             response_class=PlainTextResponse,
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
def uploadEmpProfile(emp: str = Form(...), file: UploadFile = File(...)):
    file_object = file.file
    upload_folder = open(os.path.join(UPLOAD_FOLDER, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    print("emp--------->", emp)
    empAsObject = json.loads(emp, object_hook=lambda d: SimpleNamespace(**d))
    print("Emp as Json Object: ", empAsObject)
    empObj = empService.createEmployee(empAsObject)
    json_compatible_item_data = jsonable_encoder(empObj)
    return JSONResponse(content=json_compatible_item_data, status_code=200)
