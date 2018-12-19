from flask import json


class JSONSerializable(object):

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.to_json()