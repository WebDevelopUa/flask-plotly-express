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
#
# Request: {
#     "date_range": {
#         "type": "monthly",
#         "year": 2021,
#         "month": 5,
#         "day": 12,
#         "hour": 0
#     },
#     "cid": "8546546546146"
# }
#
# Response: {
#     "nlinks": 10,
#     "hits": [12, 10, 7, ..., 40],
#     "top_ref": [
#                   {"n": "LinkedIn", "h": 12, ... , {"n": "others", "h": 20}}
#                 ],
#     "top_cntr": [
#                   {"n": "Ukraine", "h": 12, ... , {"n": "others", "h": 20}}
#                 ]
# }
#
#  Plotly EXPRESS Sample #3
# Selector options:
# Weekly - Display last 7 days
# Monthly - Display last 1 - 31 days (we need to know what is the current year + month)
# Yearly - Display all * days (we need to know what is the current year)


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
        # title='xc',
    )

    fig.update_xaxes(
        title='',
        tickangle=30,
        title_font={"size": 20},
        title_standoff=25
    )

    fig.update_yaxes(
        title_standoff=25)

    # https: // plotly.com / python / reference / layout /
    # https: // habr.com / ru / post / 502958 /
    # https: // plotly.com / python / legend /
    # fig.update_layout(),
    # fig.show(config=dict(displayModeBar=False))
    # fig.update_layout({'plot_bgcolor': "#21201f", 'paper_bgcolor': "#21201f", 'legend_orientation': "h"},
    #                   legend=dict(y=1, x=0),
    #                   font=dict(color='#dedddc'),
    #                   dragmode='pan',
    #                   hovermode='x unified',
    #                   margin=dict(b=20, t=0, l=0, r=40),
    #                   ),

    fig.update_layout(
        # hovermode=False,
        # showlegend=False,
        # dragmode=False,
        # clickmode="none",
        separators='/',
        # paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor=" #F8F9F9",
        font=dict(
            color='#000080'
        ),
        margin=dict(b=20, t=0, l=0, r=40),
        modebar=dict(
            bgcolor='rgba(256,256,256, 0.1)',
            remove=["autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", "hoverCompareCartesian",
                    "hovercompare", "lasso", "lasso2d", "orbitRotation", "orbitrotation", "pan", "pan2d", "pan3d",
                    "reset", "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup",
                    "resetScale2d", "resetViewMapbox", "resetViews", "resetcameradefault", "resetcameralastsave",
                    "resetsankeygroup", "resetscale", "resetview", "resetviews", "select", "select2d",
                    "sendDataToCloud", "senddatatocloud", "tableRotation", "tablerotation", "toImage",
                    "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage", "zoom",
                    "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMapbox", "zoomOut2d", "zoomOutGeo",
                    "zoomOutMapbox", "zoomin", "zoomout"]
        ),
    ),

    # https: // plotly.com / python / reference / layout / xaxis /
    fig.update_xaxes(
        tickmode='auto',
        # tickmode='linear',
        # tickmode='array',
        nticks=25,
        tickcolor='#FFFF00',
        visible=True,
        # color='#FF0000',
        # title=dict(
        #     text='xaxes'
        # )
    )

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


@app.route("/")
def link_clicks():
    fig = create_plot_link_clicks()
    config_1 = 2
    config_2 = 3

    return render_template("link-clicks.html", fig=fig, config_1=config_1, config_2=config_2)


if __name__ == '__main__':
    app.run()
