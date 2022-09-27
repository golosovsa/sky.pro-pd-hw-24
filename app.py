from flask import Flask, request, Response
from helpers import ServerError
from query import setup_query


def create_app():
    flask_app = Flask(__name__)

    @flask_app.route("/perform_query", methods=['POST'])
    def perform_query():
        try:
            data = request.form
            iterator = setup_query(data)
            data = list(iterator)
            return app.response_class("\n".join(data), content_type="text/plain")
        except ServerError as error:
            return str(error), 404

    return flask_app


app: Flask = create_app()



# if __name__ == "__main__":
#     app.run(debug=True)
