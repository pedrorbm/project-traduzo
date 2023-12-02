from flask import Blueprint, render_template
from models.language_model import LanguageModel
from flask import request
from deep_translator import GoogleTranslator

tradutor_controller = Blueprint("tradutor_controller", __name__)


@tradutor_controller.route("/", methods=["GET"])
def get():
    tradutor = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }

    result = render_template("index.html", **tradutor)

    return result


@tradutor_controller.route("/", methods=["POST"])
def post():
    tradutor = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": request.form["text-to-translate"],
        "translate_from": request.form["translate-from"],
        "translate_to": request.form["translate-to"],
        "translated": GoogleTranslator(
            source=request.form["translate-from"],
            target=request.form["translate-to"],
        ).translate(request.form["text-to-translate"]),
    }

    result = render_template("index.html", **tradutor)

    return result
