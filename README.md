# Airliners Comparitive Dashboard

1. **Data Ingestion & Transformation (BigQuery + dbt)**
    * The raw data is ingested and processed using dbt (Data Build Tool) for SQL-based transformations. Models are created to aggregate and clean the data for various airline performance metrics.
2. **Dashboarding using TaiPy**
    * Using TaiPy for front-end as has modular featurization which seperates SQL, visual and python layers. High responsiveness when compared with streamlit.
3. **Technologies Used**
    * **dbt:** For data transformation, materializing SQL models as tables or views in BigQuery.
    * Google BigQuery: For data storage and querying.
    * **Taipy:** For dashboard creation and visualization.
    * **Docker:** Containerizing the application for deployment and environment consistency.
    * **Python:** Core language for scripting, data handling, and dashboard creation.
Pandas: For data manipulation and analysis.

## Directory Structure

```bash
root/
├── .gitignore                     # Specifies files and directories to be ignored by Git
├── app.py                         # Main application script
├── config.py                      # Configuration settings for the project
├── dbt_project.yml                # Configuration file for the dbt (data build tool) project
├── docker-compose.yml             # Defines Docker services for multi-container Docker applications
├── Dockerfile                     # Docker setup for containerizing the application
├── README.md                      # Project overview and setup instructions
├── requirements.txt               # Python dependencies for the project
├── .vscode/                       # IDE settings for Visual Studio Code
│   └── settings.json              # VSCode-specific settings
├── data/                          # Directory for datasets, logs, and scripts
│   ├── datamaker.py               # Script to generate data
│   ├── data_processing.py         # Script for processing the data
├── models/                        # SQL models for various business insights
│   ├── average_airline_rating_by_year.sql  # SQL model for calculating average airline ratings by year
│   ├── monthly_profit_trends.sql  # SQL model for tracking monthly profit trends
│   └── revenue_breakdown_by_class_type.sql # SQL model for breaking down revenue by class type
........(see full in visualization plan)
└── merged_output.txt              # Output file for merged results


```


## Visualization Plan

| **Title**                                                        | **Best Chart Type**          | **dbt Model Name**                     | **Description**                                                    |
|------------------------------------------------------------------|------------------------------|----------------------------------------|-------------------------------------------------------------------|
| **Profits from 2023 compared with 2022**                         | Grouped Bar Chart            | `profits_comparison_2022_2023`         | Compare airline profits year-over-year (2022 vs 2023).             |
| **Most Profitable Routes Year-wise**                             | Table or Bar Chart           | `most_profitable_routes_by_year`       | Display the most profitable routes for each year.                  |
| **Average Profit Margin by Class Type**                          | Bar Chart                    | `average_profit_margin_by_class`       | Compare average profit margins across different class types.       |
| **Monthly Profit Trends**                                        | Line Chart                   | `monthly_profit_trends`                | Show trends in monthly profits for each airline.                   |
| **Average Airline Rating Comparison by Year**                    | Line Chart                   | `average_airline_rating_by_year`       | Compare airline ratings across different years (2021-2023).        |
| **Market Share by Airline**                                      | Pie Chart or Bar Chart       | `market_share_by_airline`              | Visualize each airline’s market share as a proportion of total.    |
| **Top Destinations by Passenger Volume**                         | Bar Chart or Geo Map         | `top_destinations_by_passenger_volume` | Display top destinations based on passenger volume.                |
| **Average Ticket Price by Departure City**                       | Bar Chart                    | `avg_ticket_price_by_departure_city`   | Compare average ticket prices for each departure city.             |
| **Revenue Breakdown by Class Type**                              | Grouped Bar Chart            | `revenue_breakdown_by_class_type`      | Show revenue per flight and per passenger, broken down by class.   |
| **Seasonal Passenger Trends**                                    | Line Chart                   | `seasonal_passenger_trends`            | Analyze passenger volume trends across different seasons.          |
| **Customer Satisfaction Analysis (Correlation between Rating and Profit)** | Scatter Plot with Trendline  | `customer_satisfaction_analysis`       | Examine the correlation between customer ratings and airline profit.|
| **Flight Duration Impact on Ticket Price**                       | Scatter Plot                 | `flight_duration_vs_ticket_price`      | Show the relationship between flight duration and ticket price.    |
| **Revenue by Country**                                           | Bar Chart or Geo Map         | `revenue_by_country`                   | Compare total revenue by country.                                  |
| **Total Profit by Airline Country and Number of Flights**        | Bubble Chart                 | `profit_and_flights_by_country`        | Display total profit and number of flights per country.            |
| **Underperforming Flights**                                      | Table or Bar Chart           | `underperforming_flights`              | List underperforming flights (profits below a threshold).          |

### Setting Up the Project

1. Clone the repo.
2. Ensure you have Docker installed and running.
3. Setup GCP credentials by placing your JSON file in the project root directory.
4. Navigate to data/ directory and run
```bash
dbt run
```
5. This will materialize all the SQL models into views or tables depending on how you have setup your `dbt_project.yml` file.
6. Run the dashboard by running
```bash
python app.py
```
7. Run with Docker
```bash
docker-compose up --build
```

After running `docker-compose up --build`, the application will automatically start, and you can access the dashboard (usually at [http://localhost:5000](http://localhost:5000) or the port specified in the `docker-compose.yml`).

