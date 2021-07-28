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


#  Plotly Sample

# def create_plot():
#     data = load_data()
#
#     trace1 = {
#         "x": [d["date"] for d in data],
#         "y": [d["total_tests"] for d in data],
#         "name": "trace1 - Total Tests"
#     }
#
#     trace2 = {
#         "x": [d["date"] for d in data],
#         "y": [d["total_cases"] for d in data],
#         "name": "trace2 - Total Cases"
#     }
#
#     trace3 = {
#         "x": [d["date"] for d in data],
#         "y": [d["total_deaths"] for d in data],
#         "name": "trace3 - Total Deaths"
#     }
#
#     plot_data = [trace1, trace2, trace3]
#
#     plot_layout = {
#         "title": "plot_layout - PLOT Layout Title"
#     }
#
#     data = json.dumps(plot_data, cls=plotly.utils.PlotlyJSONEncoder)
#     layout = json.dumps(plot_layout, cls=plotly.utils.PlotlyJSONEncoder)
#
#     return data, layout
#

# @app.route("/")
# def home():
#     data, layout = create_plot()
#     return render_template("index.html", data=data, layout=layout)


# @app.route("/express")
# def express():
#     fig = create_plot_express()
#     return render_template("express.html", fig=fig)

# -------------------------------------------------------

#  Plotly EXPRESS Sample #1 - LINE

def create_plot_express_clicks():
    data = load_data()
    fig = px.line(
        x=[d["date"] for d in data],
        y=[d["total_tests"] for d in data]
    )

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# -------------------------------------------------------

#  Plotly EXPRESS Sample #2

def create_plot_express_csv():
    data = load_data()
    df = px.data.gapminder().query("continent=='Canada'")
    fig = px.line(df,
                  x=[d["date"] for d in data],
                  y=[d["continent"] for d in data],
                  title='Life expectancy in Canada')
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# -------------------------------------------------------

#  Plotly EXPRESS Sample #3


def create_plot_link_clicks():
    fig = px.line(
        x=['2020-10-01',
           '2020-10-02',
           '2020-10-03',
           '2020-10-04',
           '2020-10-05',
           '2020-10-06',
           '2021-01-07',
           '2021-02-08',
           '2021-03-09'],
        y=[10, 20, 100, 50, 0, 1, 55, 25, 150],
        labels={'y': '', 'x': ''},
        title='',
    )

    fig.update_xaxes(
        tickangle=30,
        title_font={"size": 20},
        title_standoff=25
    )

    fig.update_yaxes(
        title_standoff=25)

    fig.update_layout(),
    # fig.show(config=dict(displayModeBar=False))

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# -------------------------------------------------------


@app.route("/express")
def express_csv():
    fig = create_plot_express_csv()
    return render_template("express.html", fig=fig)


@app.route("/clicks")
def clicks():
    fig = create_plot_express_clicks()
    return render_template("clicks.html", fig=fig)


@app.route("/lc")
def link_clicks():
    fig = create_plot_link_clicks()
    return render_template("link-clicks.html", fig=fig)


if __name__ == '__main__':
    app.run()
