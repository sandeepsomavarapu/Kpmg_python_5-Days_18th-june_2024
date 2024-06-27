import urllib3 #pip instlall packagename pip instlall urllib3
import json
from pprint import pprint 
encoded_body = json.dumps({"id": 555,"name": "rohit","salary":88000,"phonenumber": 999898,"company":"kpmg"})
http = urllib3.PoolManager()

headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
}
response = http.request("GET", "https://dummyjson.com/products")
pprint(response.data) # Prints 200

#making rest cal to spring boot app
# response = http.request("GET", "http://localhost:8586/employees/GetAllEmployees")

# print(response.data.decode("utf-8"))

# response = http.request("GET", "http://localhost:8586/employees/GetAllEmployees")

# print(response.data.decode("utf-8"))
# http://localhost:8586/employees/EmployeeCreation
# response = http.request("POST", "http://localhost:8586/employees/EmployeeCreation",headers={'Content-Type': 'application/json'},body=encoded_body)
# print(response.data.decode("utf-8"))
# response = http.request("POST", "http://jsonplaceholder.typicode.com/posts", fields={"title": "Created Post", "body": "kpmg india", "userId": 789})

# print(response.data.decode("utf-8"))

# response = http.request("GET",
#                         "https://fakestoreapi.com/products/1", 
#                         fields={"id": "1"})
# print(response.data.decode("utf-8"))

# response = http.request("GET",
#                         "https://fakestoreapi.com/products/1", 
#                         )
# print(response.data.decode("utf-8"))


# for i in range(1, 5):
#     response = http.request("DELETE", "http://jsonplaceholder.typicode.com/posts", fields={"id": i})
#     print(response.data.decode("utf-8"))

# print(response.data.decode("utf-8"))
#http://localhost:8586/employees/EmployeeCreation
# response = http.request("POST", "http://localhost:8080/products/addProduct", fields={"productId": 444,"productName": "intel","productPrice":7880,"productCategory": "electronics"},headers={'Content-Type': 'application/json'})
# print(response.data.decode("utf-8"))