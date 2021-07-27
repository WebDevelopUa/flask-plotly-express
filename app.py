from flask import Flask, jsonify, render_template
import csv
import os
import json
import plotly
import plotly.express as px

app = Flask(__name__)


def load_data():
    with open("./data/data.csv") as file:
        dict_reader = csv.DictReader(file)
        return list(dict_reader)


def create_plot_express():
    data = load_data()
    fig = px.line(
        x=[d["date"] for d in data],
        y=[d["total_tests"] for d in data]
    )

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def create_plot():
    data = load_data()

    trace1 = {
        "x": [d["date"] for d in data],
        "y": [d["total_tests"] for d in data],
        "name": "trace1 - Total Tests"
    }

    trace2 = {
        "x": [d["date"] for d in data],
        "y": [d["total_cases"] for d in data],
        "name": "trace2 - Total Cases"
    }

    trace3 = {
        "x": [d["date"] for d in data],
        "y": [d["total_deaths"] for d in data],
        "name": "trace3 - Total Deaths"
    }

    plot_data = [trace1, trace2, trace3]

    plot_layout = {
        "title": "plot_layout - PLOT Layout Title"
    }

    data = json.dumps(plot_data, cls=plotly.utils.PlotlyJSONEncoder)
    layout = json.dumps(plot_layout, cls=plotly.utils.PlotlyJSONEncoder)

    return data, layout


@app.route("/")
def home():
    data, layout = create_plot()
    return render_template("index.html", data=data, layout=layout)


@app.route("/express")
def express():
    fig = create_plot_express()
    return render_template("express.html", fig=fig)


if __name__ == '__main__':
    app.run()
