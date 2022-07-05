from flask import Flask

app = Flask(__name__)

@app.route('/api/Get/IP')
def Get_IP():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()