from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read in details for page
def readDetails(filepath):
    with open('myBrandNewApp/static/aboutMe.txt', 'r') as f:
        return [line for line in f]

@app.route('/')
def homepage():
    about_me_contents = readDetails('aboutMe.txt')
    return render_template('base.html', aboutMe=about_me_contents)

@app.route('/user/<name>')
def hello(name):
    return render_template('hello.html', name = name)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

# Add the option to run the file directly
if __name__ == "__main__":
    app.run(debug=True)