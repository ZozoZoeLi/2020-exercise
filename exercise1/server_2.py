import flask

app = flask.Flask(__name__)

@app.route('/two/hello')
def hello():
    resp = flask.Response("Foo bar baz")
    return resp

@app.route('/two/mediafile')
def private_file():
    resp = flask.Response("")
    resp.headers['X-Accel-Redirect'] = '/private_files/secret.txt'
    return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=19532)
