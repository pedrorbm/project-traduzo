from flask import Blueprint, render_template
from models.language_model import LanguageModel

tradutor_controller = Blueprint("tradutor_controller", __name__)


@tradutor_controller.route("/", methods=["GET"])
def get():
    translate = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?"
    }

    result = render_template(
        "index.html",
        **translate
    )

    return result
