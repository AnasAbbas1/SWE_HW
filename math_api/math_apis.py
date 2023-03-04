from flask import Flask, request, jsonify
from .apis_input_validator import APIsInputValidator
from .api_model import APIsModel

class MathAPIs:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.route('/min', methods=['POST'])(self.handle_request)
        self.app.route('/max', methods=['POST'])(self.handle_request)
        self.app.route('/avg', methods=['POST'])(self.handle_request)
        self.app.route('/median', methods=['POST'])(self.handle_request)
        self.app.route('/percentile', methods=['POST'])(self.handle_request)

    def handle_request(self):
        try:
            data = request.get_json()
            endpoint = request.path[1:] # remove leading slash from endpoint name
            quantifier_name = 'quantifier' if endpoint in ('min', 'max') else None
            quantifier_name = 'q' if endpoint == 'percentile' else quantifier_name
            APIsInputValidator.validate_input(data, quantifier_name)
            func = getattr(APIsModel, endpoint)
            result = func(data)
            return jsonify(result), 200
        except Exception as e:
            return jsonify(str(e)), 400

    def run(self):
        pass