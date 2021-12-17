import requests


class ApiPetStore:
    def __init__(self):
        self.url = "https://petstore.swagger.io"
        self.default_headers = {"Accept": "application/json"}

    # = = = = = = = = = = = [ USER ]

    def get_user(self, username):
        api_method = f"/v2/user/{username}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: GET", url, sep="\n")
        response = requests.request("GET", url, headers=headers)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def post_user(self, id, username, firstname, lastname, email, password, phone, userStatus):
        api_method = f"/v2/user"
        url = f"{self.url}{api_method}"

        req_dict = {
            "id": id,
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus
        }
        headers = self.default_headers
        headers["content-type"] = "application/json"

        print("REQUEST: POST", url, req_dict, sep="\n")
        response = requests.request("POST", url, headers=headers, json=req_dict)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def delete_user(self, username):
        api_method = f"/v2/user/{username}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: DELETE", url, sep="\n")
        response = requests.request("DELETE", url, headers=headers)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def put_user(self, username, req_dict):
        api_method = f"/v2/user/{username}"
        url = f"{self.url}{api_method}"

        headers = self.default_headers
        headers["content-type"] = "application/json"

        print("REQUEST: PUT", url, req_dict, sep="\n")
        response = requests.request("PUT", url, headers=headers, json=req_dict)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    # = = = = = = = = = = = [ PET ]

    def get_pet_by_id(self, pet_id):
        api_method = f"/v2/pet/{pet_id}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: GET", url, sep="\n")
        response = requests.request("GET", url, headers=headers)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def get_pets_by_status(self, status):
        api_method = "/v2/pet/findByStatus" + f"?status={status}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: GET", url, sep="\n")
        response = requests.request("GET", url, headers=headers)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def post_pet(self, id, category, name, photoUrls, tags, status):
        api_method = f"/v2/pet"
        url = f"{self.url}{api_method}"

        req_dict = {
            "id": id,
            "category": category,
            "name": name,
            "photoUrls": photoUrls,
            "tags": tags,
            "status": status
        }
        headers = self.default_headers
        headers["content-type"] = "application/json"

        print("REQUEST: POST", url, req_dict, sep="\n")
        response = requests.request("POST", url, headers=headers, json=req_dict)
        print("RESPONSE: ", response.status_code, response.text, sep="\n")
        return response

    def delete_pet(self, pet_id):
        api_method = f"/v2/pet/{pet_id}"
        url = f"{self.url}{api_method}"
        headers = self.default_headers

        print("REQUEST: DELETE", url, sep="\n")
        response = requests.request("DELETE", url, headers=headers)
        print("RESPONSE: DELETE", response.status_code, response.text, sep="\n")
        return response

