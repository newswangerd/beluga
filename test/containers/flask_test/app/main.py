from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    f = open('times', 'r')
    times = int(f.read())
    times += 1
    f.close()
    f = open('times', 'w')
    f.write(str(times))
    f.close()

    assert(times > 2)
    return "HEALTHY"
