from flask import Blueprint
from models.history_model import HistoryModel

historico_controller = Blueprint("historico_controller", __name__)


@historico_controller.route('/', methods=['GET'])
def get():
    history_model = HistoryModel.list_as_json()

    return history_model, 200
