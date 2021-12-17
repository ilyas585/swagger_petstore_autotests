import random
import string


class MessageHelper:

    @staticmethod
    def generate_added_string(original_str, added_max_len=20, added_min_len=0):
        symbols = string.ascii_letters + string.digits
        return original_str + "".join([random.choice(symbols) for i in range(
            random.randrange(added_min_len, added_max_len))])

    def generate_email(self, prefix):
        return f"{self.generate_added_string(f'{prefix}_', added_min_len=10)}@email.com"

    @staticmethod
    def generate_phone():
        return f"+7800{random.randint(1000000, 9999999)}"

    def generate_name(self, prefix=''):
        return self.generate_added_string(f'{prefix}', added_min_len=10)

    def generate_password(self):
        res_str1 = f"{self.generate_added_string('', 5, 3)}"
        res_str2 = f"{self.generate_added_string('', 5, 3)}"
        res_str3 = f"{self.generate_added_string('', 5, 3)}"
        return res_str1 + res_str2 + res_str3
