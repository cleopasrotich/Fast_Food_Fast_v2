from flask import Flask, jsonify


def create_app(config_name):

    app = Flask(__name__)



    @app.errorhandler(404)
    def error1(error):
        return jsonify({"Page not found"}), 404

    @app.errorhandler(500)
    def error_2(error):
        return jsonify({"There seem to be a problem with your server."}), 404
    return app
