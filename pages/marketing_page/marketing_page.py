from taipy.gui import Markdown
from data.data_processing import get_dataframe

# Fetch the data for the tables
m1 = get_dataframe('top_destinations_by_passenger_volume')
m2 = get_dataframe('avg_ticket_price_by_departure_city')
m3 = get_dataframe('revenue_breakdown_by_class_type')
m4 = get_dataframe('seasonal_passenger_trends')
m5 = get_dataframe('customer_satisfaction_analysis')

# Create the Markdown content
Marketing = Markdown("""
<center>
    <|navbar|lov={[('/overview', 'Overview'), ('/marketing', 'Marketing')]}|>
</center>

                     
# Marketing Page

This page provides insights into the airline's marketing performance.

## Top Destinations by Passenger Volume
<|{m1}|table|>
                     
## Average Ticket Price by Departure City
<|{m2}|table|>

## Revenue Breakdown by Class Type
<|{m3}|table|>

## Seasonal Passenger Trends
<|{m4}|table|>

## Customer Satisfaction Analysis
<|{m5}|table|>
""")
