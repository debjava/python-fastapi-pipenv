import json
from types import SimpleNamespace
from typing import Optional
from fastapi import APIRouter, Response, Form, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse

from app.entity.Employee import Employee
from app.services import EmployeeServices as empService

router = APIRouter()


# Using employee as json localhost:8090/createEmp
@router.post('/createEmp',
             tags=["HTTP POST Method Usage"],
             description="Creates a new employee by sending json body",
             summary="Creates a new employee by sending json body",
             response_class=JSONResponse,
             responses={
                 400: {
                     "content": {"application/json": {}},
                     "description": "Bad Request or Operation forbidden",
                 },
                 500: {
                     "content": {"plain/text": {}},
                     "description": "Internal Server Error.",
                 }
             },
             )
def createEmployee(emp: Employee):
    empService.createEmployee(emp)
    json_compatible_item_data = jsonable_encoder(emp)
    return JSONResponse(content=json_compatible_item_data, status_code=200)


# # Using form parameter
@router.post("/saveEmp",
             tags=["HTTP POST Method Usage"],
             description="Saves employee info by sending id, fName and lName as form parameters",
             summary="Saves employee info by sending id, fName and lName as form parameters",
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
def saveEmp(id: str = Form(...), fName: str = Form(...), lName: str = Form(...)):
    emp = Employee()
    emp.empId = id
    emp.firstName = fName
    emp.lastName = lName
    print("Employee as object: ", emp)
    resData = "Employee info saved successfully"
    return Response(content=resData, status_code=200, media_type="plain/text")
#
# Using key as Header
@router.post("/createEmpKey",
             tags=["HTTP POST Method Usage"],
             description="Create employee by sending security key as header",
             summary="Create employee by sending security key as header",
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
def createEmployeeKey(emp: Employee, key: Optional[str] = Header(None)):
    print("Received Key as Header: ", key)
    empService.createEmployee(emp)
    resData = "Employee key accepted and created successfully"
    return Response(content=resData, status_code=200, media_type="plain/text")
