import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def make_data():
    """
    Generates an airline dataset with 1000 rows, including various columns
    suitable for practicing SQL queries such as rank, dense rank, datetime functions,
    profits, group by case when, and other operations.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the generated dataset.
    """
    num_rows = 1000

    # Airline IDs from 1 to 10
    airline_ids = np.random.randint(1, 11, size=num_rows)

    # Airline names corresponding to airline IDs
    airline_names_list = [
        'Air Alpha', 'Bravo Airlines', 'Charlie Air', 'Delta Flights', 'Echo Airways',
        'Foxtrot Aviation', 'Golf Airlines', 'Hotel Air', 'India International', 'Juliet Jet'
    ]
    airline_names = [airline_names_list[id - 1] for id in airline_ids]

    # Airline ratings between 1.0 and 5.0
    airline_ratings = np.round(np.random.uniform(1.0, 5.0, size=num_rows), 1)

    # Airline countries from a predefined list
    countries = ['USA', 'UK', 'France', 'Germany', 'Canada', 'Australia', 'Japan', 'China', 'India', 'Brazil']
    airline_countries = [random.choice(countries) for _ in range(num_rows)]

    # Random flight dates within the last 2 years
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = (end_date - start_date).days
    flight_dates = [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(num_rows)]

    # Departure and arrival cities from a predefined list
    cities = ['New York', 'London', 'Paris', 'Berlin', 'Toronto', 'Sydney', 'Tokyo', 'Beijing', 'Mumbai', 'Sao Paulo']
    departure_cities = [random.choice(cities) for _ in range(num_rows)]
    arrival_cities = [random.choice([city for city in cities if city != dep_city]) for dep_city in departure_cities]

    # Flight durations between 1 and 15 hours
    flight_durations = np.round(np.random.uniform(1, 15, size=num_rows), 2)

    # Number of passengers between 50 and 300
    number_of_passengers = np.random.randint(50, 301, size=num_rows)

    # Ticket prices between $100 and $2000
    ticket_prices = np.round(np.random.uniform(100, 2000, size=num_rows), 2)

    # Costs between $5000 and $100,000
    costs = np.round(np.random.uniform(5000, 100000, size=num_rows), 2)

    # Total revenue and profit calculations
    total_revenues = np.round(number_of_passengers * ticket_prices, 2)
    profits = np.round(total_revenues - costs, 2)

    # Flight statuses
    flight_statuses = [random.choices(['On Time', 'Delayed', 'Cancelled'], weights=[0.7, 0.2, 0.1])[0] for _ in range(num_rows)]

    # Class types
    class_types = [random.choices(['Economy', 'Business', 'First Class'], weights=[0.7, 0.2, 0.1])[0] for _ in range(num_rows)]

    # Create the DataFrame
    df = pd.DataFrame({
        'airline_id': airline_ids,
        'airline_name': airline_names,
        'airline_rating': airline_ratings,
        'airline_country': airline_countries,
        'flight_date': flight_dates,
        'departure_city': departure_cities,
        'arrival_city': arrival_cities,
        'flight_duration': flight_durations,
        'number_of_passengers': number_of_passengers,
        'ticket_price': ticket_prices,
        'total_revenue': total_revenues,
        'costs': costs,
        'profit': profits,
        'flight_status': flight_statuses,
        'class_type': class_types
    })

    return df

# Generate the dataset
df = make_data()

# Save to parquet file
df.to_parquet('airline_data.parquet', index=False)