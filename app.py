from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blockchain101')
def blockchain101():
    return render_template('blockchain101.html')

@app.route('/futureofshopping')
def future_of_shopping():
    return render_template('futureofshopping.html')

@app.route('/demo')
def interactive_demo():
    return render_template('interactive_demo.html')

@app.route('/tips')
def safe_shopping_tips():
    return render_template('safe_shopping_tips.html')

@app.route('/policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/tos')
def terms_of_service():
    return render_template('terms_of_service.html')

if __name__ == "__main__":
    app.run(debug=True)
