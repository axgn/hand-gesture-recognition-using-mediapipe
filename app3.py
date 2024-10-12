from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_json():
    if request.is_json:
        data = request.get_json()
        print(f'Received JSON data: {data}')
        return jsonify({'status': 'success', 'data': data}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400


if __name__ == '__main__':
    app.run(debug=True)
