from bottle import *
import urllib.request, json
import os


with urllib.request.urlopen("http://apis.is/concerts") as url:
    data = json.loads(url.read().decode())

@route("/")
def index():
    return template('index.tpl', data=data)

@route("/static/<file>")
def static_skrar(file):
    return static_file(file, root='./')


@error(404)
def error404(error):
    return '<p>This webside dose not exist</p><a href="/">back</>'

run(host='0.0.0.0', port=os.environ.get('PORT'))
