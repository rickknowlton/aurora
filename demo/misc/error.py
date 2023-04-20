class A:
    def __init__(oop, a):
        oop.a = a

from flask import Flask, jsonify, make_response, request

app = Flask('python-flask-seed')


@app.route('/oop', methods=['POST'])
def oop:
    content = request.get_json(silent=True, force=True)

    try:
        message = 'oop %s!' % content['oop']
        response = {'message': message}
        return make_response(jsonify(response), 200)

    except Exception as ex:
        response = {'error': 'oop is required'}
        return make_response(jsonify(response), 400)