from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/event management')
def login():
    return render_template('event management.html')

@app.route('/services')
def books():
    return render_template('services.html')

if __name__== '__main__':
    app.run(debug=True)