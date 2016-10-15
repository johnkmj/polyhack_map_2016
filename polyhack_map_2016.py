import os
import xml.etree.ElementTree
import json
from flask import Flask, request, send_from_directory, render_template
from gen_res import generate_graph, gen_shortest_path, read_nodes

app = Flask(__name__, static_url_path='')


def import_floors(path):
    floor = []
    if path == '1F_path.svg':
        with open('img/1F_path.svg') as inputfile:
            for line in inputfile:
                floor.append(line)
    elif path == '2F_path.svg':
        with open('img/2F_path.svg') as inputfile:
            for line in inputfile:
                floor.append(line)
    elif path == '3F_path.svg':
        with open('img/3F_path.svg') as inputfile:
            for line in inputfile:
                floor.append(line)
    elif path == '4F_path.svg':
        with open('img/4F_path.svg') as inputfile:
            for line in inputfile:
                floor.append(line)

    res = '\n'.join([str(line) for line in floor])
    return res


@app.route('/map/', methods=['POST'])
def hello():
    start = request.form['start']
    end = request.form['end']
    print(start)
    print(end)
    path = generate_graph(start, end)
    csv_res = ""
    for node in path:
        csv_res += node
        csv_res += ","
    csv_res = csv_res[:-1]
    print csv_res
    return csv_res


@app.route('/img/<path:path>')
def send_img(path):
    return import_floors(path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def root():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True)
