from client.petstore import ApiPetStore
from helper.message import MessageHelper
from checker.general import Checker


class Application:
    def __init__(self):
        self.api = ApiPetStore()
        self.helper = MessageHelper()
        self.checker = Checker()

