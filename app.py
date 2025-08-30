from flask import Flask, render_template, request
import main  # Assuming main.py contains your core logic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        option = request.form.get('option')
        input_type = request.form.get('type')
        if option == 'reverse':
            processed = user_input[::-1]
        else:
            processed = main.process_input(user_input) if hasattr(main, 'process_input') else f"Echo: {user_input}"
        result = f"Type: {input_type} | {processed}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
