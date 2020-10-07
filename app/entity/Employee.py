from pydantic import BaseModel


class Employee(BaseModel):
    empId: str = None
    firstName: str = None
    lastName: str = None

    def __str__(self):
        return str(self.empId) + " " + self.firstName + " " + self.lastName
