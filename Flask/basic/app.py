from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "<h1> Welcome to Digital Cloud Nest</h1>"
    return render_template("home.html")

@app.route('/about')
def about():
    #return "<h1>Technology Engineering Operations</h1>"   
    return render_template("about.html") 

@app.route('/plot')
def plot():
    from pandas_datareader import data
    import datetime
    import dateutil.relativedelta
    import quandl
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN    

    start = datetime.datetime.now() - dateutil.relativedelta.relativedelta(days=30)
    end   = datetime.datetime.now()
    quandl.read_key()
    infy_stock =data.DataReader('BSE/BOM500209', 'quandl',api_key=quandl.ApiConfig.api_key, 
                                 start = start, end = end)

    infy_stock["Status"]   = ["Increase" if c > o else "Decrease" if c < o else "Equal" 
                            for c,o in zip(infy_stock.Close,infy_stock.Open)]
    infy_stock["Midpoint"] = (infy_stock.Open + infy_stock.Close)/2
    infy_stock["Height"]   = abs(infy_stock.Open - infy_stock.Close)

    plot_i = figure(x_axis_type = 'datetime', width = 800, height = 300, sizing_mode = "scale_width")
    plot_i.title.text = "Candlestick Chart of Infosys"
    plot_i.grid.grid_line_alpha = 0.5

    hours_12 = 12*60*60*1000

    plot_i.segment(infy_stock.index, infy_stock.High, infy_stock.index, infy_stock.Low, color="magenta")

    plot_i.rect(infy_stock.index[infy_stock.Status == "Increase"], infy_stock.Midpoint[infy_stock.Status == "Increase"], 
                hours_12, infy_stock.Height[infy_stock.Status == "Increase"], fill_color="green", line_color="black")

    plot_i.rect(infy_stock.index[infy_stock.Status == "Decrease"], infy_stock.Midpoint[infy_stock.Status == "Decrease"], 
                hours_12, infy_stock.Height[infy_stock.Status == "Decrease"], fill_color="red", line_color="black")

    plot_i.rect(infy_stock.index[infy_stock.Status == "Equal"], infy_stock.Midpoint[infy_stock.Status == "Equal"], 
                hours_12, infy_stock.Height[infy_stock.Status == "Equal"], fill_color="blue", line_color="black")

    script1, div1 = components(plot_i)
    cdn_js = CDN.js_files
    cdn_css = CDN.css_files

    return render_template("plot.html", script1 = script1, div1 = div1, cdn_js = cdn_js, cdn_css = cdn_css)

if __name__ == "__main__":
    app.run()    