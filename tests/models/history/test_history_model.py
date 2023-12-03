import json
# from src.models.language_model import LanguageModel
from src.models.history_model import HistoryModel

result = [
    {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    },
    {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    },
]


def test_request_history():
    history_model = HistoryModel.list_as_json()
    load = json.loads(history_model)
    string = type(history_model)
    test_one = load[1]["text_to_translate"]
    test_two = load[0]["text_to_translate"]
    result_one = result[1]["text_to_translate"]
    result_two = result[0]["text_to_translate"]

    try:
        history_model = HistoryModel.list_as_json()
        load = json.loads(history_model)
        string = type(history_model)
        test_one = load[1]["text_to_translate"]
        test_two = load[0]["text_to_translate"]
        result_one = result[1]["text_to_translate"]
        result_two = result[0]["text_to_translate"]

        assert test_one == result_one

        assert test_two == result_two

        assert string is str
    except ValueError:
        assert test_one == result_one

        assert test_two == result_two

        assert string is str
