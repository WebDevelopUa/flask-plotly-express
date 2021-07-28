# Flask + Plotly + Plotly Express

For simple visualizations that don't need interactivity with your page, this pattern with Flask and Plotly is a great
solution. You get all the nice D3 features, like hover text events, without limiting your available production paths.

## Run project:

``` 
\venv\Scripts\python.exe -m flask run
```

Result: [127.0.0.1:5000](http://127.0.0.1:5000/)

## Links:

* [Create a Plotly Data Visualization App Using One Line of JS](https://towardsdatascience.com/create-a-plotly-data-visualization-app-using-one-line-of-js-b1865391faa4)
* [p6w-6-python-only](https://github.com/edkrueger/p6w-6-python-only)
* [Plotly Python Open Source Graphing Library](https://plotly.com/python/)
* [Plotly Express](https://github.com/plotly/plotly_express)
* [Plotly Express in Python](https://plotly.com/python/plotly-express/)

## Install

``` 
pip install plotly
pip install plotly_express
```

## Tips

Be sure to serialize JSON with cls=plotly.utils.plotlyJSONEncoder.

``` 
data = json.dumps(plot_data, cls=plotly.utils.plotlyJSONEncoder)

layout = json.dumps(plot_layout, cls=plotly.utils.plotlyJSONEncoder)
```

Use Jinja to bring JSON data into HTML, as seen here.

``` 
<script>
     const data = {{data | safe}}
     const layout = {{layout | safe}}
     Plotly.newPlot(data, layout)
</script>
```

The above code can be refactored into a single line of JavaScript.

``` 
<script>
Plotly.newPlot("myPlot", {{data | safe}}, {{layout | safe}})
</script>
```

Further simplifying our code with Plotly Express. Now instead of creating a layout and traces for our visualization, we
simply need to generate a ‘fig’ based on the Plotly Express documentation.

```
import plotly.express as px

def create_plot_express():
data = load_data()
    fig = px.line(
        x=[d["date"] for d in data],
        y=[d["total_tests"] for d in data]
    )
    
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
```

Similarly, we use the plotly.utils.PlotlyJSONEncoder to properly serialize our JSONs before templating them into the
HTML document.

``` 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    Index
    <div id="myPlot"></div>
</body>
<script>
    Plotly.newPlot("myPlot", {{ fig | safe }})
</script>
</html>
```

## Getting Started in JavaScript

* [link](https://plotly.com/javascript/getting-started/)