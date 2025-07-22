import requests
import datetime as dt
import os

USERNAME = "sameer281187"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "codingraph28"

create_user_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url= create_user_endpoint, json=user_params)
# print(response.text)

create_graph_endpoint = f"{create_user_endpoint}/{USERNAME}/graphs"

req_header = {
    "X-USER-TOKEN" : TOKEN
}

graph_params = {
    "id" : "codingraph28",
    "name" : "Python Coding",
    "unit" : "hrs",
    "type" : "float",
    "color" : "momiji",
}

# create_graph_response = requests.post(url=create_graph_endpoint, json=graph_params, headers=req_header)
# print(create_graph_response.text)

post_pixel_endpoint = f"{create_graph_endpoint}/{GRAPH_ID}"
today_date = dt.date.today().strftime("%Y%m%d")
work_quantity = input(f"Enter the no. of hours spent of python coding today ({today_date}): ")

post_pixel_param = {
    "date" : today_date,
    "quantity" : work_quantity,
}

post_pixel_resp = requests.post(url=post_pixel_endpoint, json=post_pixel_param, headers=req_header)
print(post_pixel_resp.text)

# update_pixel_endpoint = f"{post_pixel_endpoint}/20250721"
#
# update_pixel_param = {
#     "quantity": work_quantity,
# }
#
# resp = requests.put(url=update_pixel_endpoint, json=update_pixel_param, headers=req_header)
# print(resp.text)
