import os
import xml.etree.ElementTree
import pandas as pd
from flask import Flask, request, send_from_directory, render_template
from gen_res import generate_graph, gen_shortest_path

app = Flask(__name__, static_url_path='')


# node_path = ["RM_402", "H1", "H2", "H3", "H4", "H5", "RR_M1"]
def svg_gen(node_path):
    svg = xml.etree.ElementTree.parse('4F.svg')
    e = svg.getroot()

    src = "./*[@id='edges']/"
    edges = e.findall(src)

    for edge in edges:
        for i in range(len(node_path)-1):
            if(edge.attrib['id'] == node_path[i]+"-"+node_path[i+1] or
                    edge.attrib['id'] == node_path[i+1]+"-"+node_path[i]):
                edge.attrib['stroke'] = "red"

    nodes = e.findall(".//*[@id='"+node_path[0]+"']")[0].attrib['fill'] = "red"
    nodes = e.findall(
        ".//*[@id='"+node_path[-1]+"']")[0].attrib['fill'] = "red"
    svg.write("4F_path.svg")


@app.route('/map/', methods=['POST'])
def hello():
    start = request.form['start']
    end = request.form['end']
    try:
        path = gen_shortest_path(start, end)
        svg_gen(path)
        return app.send_static_file("4F_path.svg")
    except:
        return "Oops! Typo?"


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
    generate_graph()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True)
