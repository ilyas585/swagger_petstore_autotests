import json
import jsonschema

from configuration import base_path


class Checker:
    @staticmethod
    def check_field_value(data_dict, key, exp_value):
        if exp_value is not None:
            if data_dict[key] != exp_value:
                return f"значение поля {key} = {data_dict[key]} не совпало с ожидаемым = {exp_value}"
        return True

    def check_post_pet(self, resp_dict, exp_id, exp_category, exp_name,
                       exp_photoUrls, exp_tags, exp_status):
        res_set = {self.check_field_value(resp_dict, "id", exp_id),
                   self.check_field_value(resp_dict, "category", exp_category),
                   self.check_field_value(resp_dict, "name", exp_name),
                   self.check_field_value(resp_dict, "photoUrls", exp_photoUrls),
                   self.check_field_value(resp_dict, "tags", exp_tags),
                   self.check_field_value(resp_dict, "status", exp_status)}

        if res_set == {True}:
            return True
        else:
            res_str = "Некорректное тело ответа: "
            for i in res_set:
                if isinstance(i, str):
                    res_str += f"{i}; "
            return f"{res_str[:-2]}."

    @staticmethod
    def check_find_pets_by_status(resp_dict, exp_status):
        for item in resp_dict:
            if item['status'] != exp_status:
                return False
        return True

    @staticmethod
    def validate_json(item, path_to_schema):
        path = base_path + "/" + path_to_schema
        with open(path) as file:
            schema = json.load(file)

        jsonschema.validate(item, schema)
        return True

