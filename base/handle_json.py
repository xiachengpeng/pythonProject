import json


class HandleJson:
    """
    获取数据
    """

    def load_json(self):
        with open("/coding/cookie.json") as fp:
            data = json.load(fp)
        return data

    def get_data(self):
        return self.load_json()

    def write_data(self, data):
        with open("/coding/cookie.json") as fp:
            fp.write(json.dumps(data))


handle_json = HandleJson()
