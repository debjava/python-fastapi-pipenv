from fastapi import APIRouter, Response
from starlette.responses import PlainTextResponse

from app.entity.Employee import Employee

router = APIRouter()

@router.delete("/deleteEmp/{empId}",
               tags=["Employee Info Deletion"],
               description="Delete an employee by empId",
               summary="Delete an employee by empId",
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
               },)
def deleteEmp(empId: str):
    emp = Employee()
    emp.empId = empId
    emp.firstName = "DD"
    emp.lastName = "Mishra"
    resData = "Employee info deleted successfully"
    return Response(content=resData, status_code=200, media_type="plain/text")
