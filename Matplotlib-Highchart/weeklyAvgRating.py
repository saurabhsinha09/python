import justpy as jp
from pandas.core.dtypes.common import classes
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates = ['Timestamp'])

data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'These graphs represent course review analysis'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a = web_page, text = "Analysis of Course Reviews", 
                 classes = "text-h1 text-center q-pa-md")

    hc = jp.HighCharts(a = web_page, options = chart_def)
    #print(hc.options)
    #print(type(hc.options))

    hc.options.title.text = 'Average Rating by Week'
    hc.options.series[0].name = 'Weekly Rating'
    hc.options.xAxis.categories = list(week_average.index)
    #hc.options.series[0].data = list(zip(day_average.index, day_average['Rating']))
    hc.options.series[0].data = list(week_average['Rating'])

    return web_page

jp.justpy(app)    