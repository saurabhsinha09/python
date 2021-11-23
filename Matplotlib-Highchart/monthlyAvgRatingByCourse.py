import justpy as jp
from pandas.core.dtypes.common import classes
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("reviews.csv", parse_dates = ['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
#month_average_by_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()
month_average_by_crs = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 35,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    web_page = jp.QuasarPage()
    h1 = jp.QDiv(a = web_page, text = "Analysis of Course Reviews", 
                 classes = "text-h1 text-center q-pa-md")

    hc = jp.HighCharts(a = web_page, options = chart_def)

    hc.options.title.text = 'Monthly Average Rating by courses'
    #hc.options.series[0].name = 'Monthly Rating'
    hc.options.xAxis.categories = list(month_average_by_crs.index)
    hc_data = [{"name":v1, "data":[round(v2,2) for v2 in month_average_by_crs[v1]]} for v1 in month_average_by_crs.columns]
    hc.options.series = hc_data

    return web_page

jp.justpy(app)    