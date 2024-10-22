from taipy.gui import Markdown
import taipy.gui.builder as tgb
from data.data_processing import get_dataframe
import pandas as pd

# Fetch the data for the overview tables
o1 = get_dataframe('market_share_by_airline')
o2 = get_dataframe('most_profitable_routes_by_year')
o3 = get_dataframe('average_profit_margin_by_class')
o4 = get_dataframe('monthly_profit_trends')
o5 = get_dataframe('average_airline_rating_by_year')

layout = {
    "annotations": [],
    "xaxis": {"ticks": "", "side": "top"},
    "yaxis": {"ticks": "", "ticksuffix": " "}
}

# Edits for o2

departure_cities = o2["departure_city"]
arrival_cities = o2["arrival_city"]

for city in range(len(arrival_cities)):
    for season in range(len(departure_cities)):
        profit = o2["profit"][city]
        annotation = {
            "x": departure_cities[season],
            "y": arrival_cities[city],
            "text": f"${profit:.2f}",
            "font": {"color": "white" if profit < 0 else "black"},
            "showarrow": False
        }
        layout["annotations"].append(annotation)


# Edits for o5
# Melt the o5 DataFrame to convert the year columns into a single column
o5_melted = pd.melt(o5, 
                    id_vars=["airline_name", "trend"], 
                    value_vars=["_2021", "_2022", "_2023"], 
                    var_name="year", 
                    value_name="Rating")

# Create the Markdown content
Overview = Markdown("""
<center>
    <|navbar|lov={[('/overview', 'Overview'), ('/marketing', 'Marketing')]}|>
</center>
                    
# Overview Page

This page provides an overview of key airline performance metrics.

## Market Share by Airlines
                    
<|layout|columns=1 1|
<|
<|{o1}|table|>
|>

<|
<|{o1}|chart|type=pie|values=market_share|labels=airline_name|>
|>
|>


## Most Profitable Routes by Year
                    
<|layout|columns=1 1|
<|
<|{o2}|table|>
                    
|>
<|{o2}|chart|type=heatmap|z=profit|x=departure_city|y=arrival_city|layout={layout}|>
|>


## Average Profit Margin by Class Type
<|{o3}|table|>

## Monthly Profit Trends

<|{o4}|table|>

## Average Airline Rating by Year
<|{o5}|table|>
## Average Airline Rating by Year

<|{o5_melted}|table|>
<|{o5_melted}|chart|mode=lines|x=year|y=Rating|color=airline_name|title="Airline Ratings from 2021 to 2023"|>

""")
