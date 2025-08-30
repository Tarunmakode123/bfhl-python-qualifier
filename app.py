from flask import Flask, render_template, request
import main  # Assuming main.py contains your core logic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Example: get input from form and process with main.py logic
        user_input = request.form.get('user_input')
        # Replace the next line with actual function call from main.py
        result = main.process_input(user_input) if hasattr(main, 'process_input') else f"Echo: {user_input}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
