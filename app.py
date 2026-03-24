from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    user_input = data.get('password', '').strip()

    correct_password = read_file('pw.txt')
    link = read_file('link.txt')

    if correct_password is None:
        return jsonify({'success': False, 'message': 'Ошибка сервера: файл пароля не найден'}), 500

    if link is None:
        return jsonify({'success': False, 'message': 'Ошибка сервера: файл ссылки не найден'}), 500

    if user_input == correct_password:
        return jsonify({'success': True, 'link': link})
    else:
        return jsonify({'success': False, 'message': 'Неверный ответ. Попробуйте ещё раз.'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
