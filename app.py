from flask import Flask
app = Flask(__name__)

#@app.route('/')
#def home():
    #return "Hello My First Web Application"

@app.route('/')
def login():
    return render_tamplate('login.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)