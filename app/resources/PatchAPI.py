
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.entity.Employee import Employee

router = APIRouter()

@router.patch("/updatePartialEmp",
              tags=["HTTP PATCH Method Usage"],
              description="Update the employee by partial information",
              summary="Update the employee by partial information",
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
              },
              )
def updatePartialInfo(id: int, login: str):
    print("ID in patch request: ", id)
    print("Login Name in patch request: ", login)
    emp = Employee()
    emp.empId = id
    emp.firstName = login
    emp.lastName = "Mishra"
    json_compatible_item_data = jsonable_encoder(emp)
    return JSONResponse(content=json_compatible_item_data, status_code=200)