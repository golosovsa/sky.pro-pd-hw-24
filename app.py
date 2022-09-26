from flask import Flask, request
from helpers import ServerError
from main import setup_iterators

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        data = request.form
        it = setup_iterators(data)
        return app.response_class("\n".join(list(it)), content_type="text/plain")
    except ServerError as e:
        return 404, str(e)


