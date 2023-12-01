from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["langauges"]

    def __init__(self, dict: dict):
        super().__init__(dict)
