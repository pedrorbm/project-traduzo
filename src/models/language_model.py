from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, dict: dict):
        super().__init__(dict)

    def to_dict(self):
        result = {"name": self.data["name"], "acronym": self.data["acronym"]}

        return result

    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find()
        result = [
            cls(data).to_dict()
            for data in languages
        ]

        return result
