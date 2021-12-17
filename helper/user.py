import random

from .message import MessageHelper
from client.petstore import ApiPetStore


class UserHelper:
    def __init__(self):
        self.api = ApiPetStore()
        self.message = MessageHelper()

    def create_user(self):
        user_id = random.randint(100, 999)
        username = self.message.generate_name("Ilyas")
        firstName = self.message.generate_name("Ilyas")
        lastName = self.message.generate_name("Ilyas")
        email = self.message.generate_email("Ilyas")
        password = self.message.generate_password()
        phone = self.message.generate_phone()

        resp = self.api.post_user(user_id, username, firstName, lastName, email, password, phone, 0)
        if resp.status_code == 200:
            return username
