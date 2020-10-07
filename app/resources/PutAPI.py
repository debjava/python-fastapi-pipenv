from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.entity.Employee import Employee

router = APIRouter()


@router.put("/updateEmp1",
            tags=["HTTP PUT Method Usage"],
            description="Update employee info by sending json as body",
            summary="Update employee info by sending json as body",
            response_class=JSONResponse,
            responses={
                400: {
                    "content": {"plain/text": {}},
                    "description": "Bad Request or Operation forbidden",
                },
                500: {
                    "content": {"plain/text": {}},
                    "description": "Internal Server Error.",
                }
            }, )
def updateEmployee(emp: Employee):
    print("Employee Id: ", emp.empId)
    print("Employee First Name: ", emp.firstName)
    print("Employee Last Name: ", emp.lastName)
    json_compatible_item_data = jsonable_encoder(emp)
    return JSONResponse(content=json_compatible_item_data, status_code=200)
