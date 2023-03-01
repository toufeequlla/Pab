import json
import os


class Json:
    @staticmethod
    def read(filepath):
        f = open(filepath)
        data = json.load(f)
        f.close()
        return data

    @staticmethod
    def get_data(filename, var, key=None):
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        if key is not None:
            with open(PATH(filename)) as f:
                return json.load(f)[var][key]
        else:
            with open(filename) as f:
                return json.load(f)[var]

    @staticmethod
    def get(jsondata, key):
        try:
            if jsondata is None or key is None or jsondata == "" or key == "":
                return None
            value = jsondata
            if '<dynamic>' in key and value[key] is not None:
                return value[key]
            keys = key.split('>')
            for k in keys:
                value = value[k]
            return value
        except Exception as e:
            return None
