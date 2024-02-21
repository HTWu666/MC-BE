from flask import Flask, jsonify
from blueprints.tasks import task_bp

app = Flask(__name__)


app.register_blueprint(task_bp, url_prefix="/api")


# page not found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "This page does not exist", "error": str(error)}), 404


# global error handler
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"message": "An error occurred", "error": str(error)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
