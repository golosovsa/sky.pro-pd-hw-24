from flask import Flask, request
from helpers import ServerError
from query import setup_query

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        data = request.form
        it = setup_query(data)
        data = list(it)
        return app.response_class("\n".join(data), content_type="text/plain")
    except ServerError as error:
        return str(error), 404


# if __name__ == "__main__":
#     app.run(debug=True)
