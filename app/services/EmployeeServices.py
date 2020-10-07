from app.entity.Employee import Employee


def getEmployees():
    empList = []
    emp = Employee()
    emp.empId = 11
    emp.firstName = "John"
    emp.lastName = "Abraham"

    empList.append(emp)

    emp = Employee()
    emp.empId = 13
    emp.firstName = "DD"
    emp.lastName = "Mishra"
    empList.append(emp)

    return empList

def createEmployee(emp):
    print("Employee as Object: ", emp)
    print("Employee ID: ", emp.empId)
    print("Employee First Name: ", emp.firstName)
    print("Employee Last Name: ", emp.lastName)
    return emp

def updateEmployee(emp):
    print("Employee as Object: ", emp)
    print("Employee ID: ", emp.empId)
    print("Employee First Name: ", emp.firstName)
    print("Employee Last Name: ", emp.lastName)
    return emp