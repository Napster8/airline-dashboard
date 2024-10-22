WITH monthly_profits AS (
        SELECT airline_name, EXTRACT(MONTH FROM flight_date) as month,
                   SUM(profit) as total_monthly_profit,
                   COUNT(*) as number_of_flights
        FROM `airline-438510.airlines.airlines`
        GROUP BY airline_name, month
)
SELECT airline_name,
           ROUND(AVG(total_monthly_profit), 2) as avg_monthly_profit,
           ROUND( AVG(number_of_flights), 2)  as avg_no_of_flights
FROM monthly_profits
GROUP BY airline_name
ORDER BY avg_monthly_profit DESC
