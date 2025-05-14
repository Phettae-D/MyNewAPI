# server.py
from flask import Flask, request, jsonify
import sys
import io

PythonAPI = Flask(__name__)

@PythonAPI.route('/run', methods=['POST'])
def run_code():
    code = request.json.get("code", "")
    output = io.StringIO()
    try:
        sys.stdout = output
        exec(code, {})
        sys.stdout = sys.__stdout__
        return jsonify({"output": output.getvalue()})
    except Exception as e:
        sys.stdout = sys.__stdout__
        return jsonify({"output": f"Error: {str(e)}"})

if __name__ == "__main__":
    PythonAPI.run(host='0.0.0.0')
