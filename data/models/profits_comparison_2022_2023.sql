WITH profits23 as (
SELECT airline_name, SUM(profit) AS profit_2023
FROM `airline-438510.airlines.airlines`
WHERE EXTRACT(YEAR FROM flight_date) = 2023
GROUP BY airline_name
),
profits22 as (
SELECT airline_name, SUM(profit) AS profit_2022
FROM `airline-438510.airlines.airlines`
WHERE EXTRACT(YEAR FROM flight_date) = 2022
GROUP BY airline_name
)

SELECT p23.airline_name, p23.profit_2023, p22.profit_2022, p23.profit_2023 - p22.profit_2022 as profit_diff
FROM profits23 p23
JOIN profits22 p22 ON p23.airline_name = p22.airline_name
ORDER BY profit_diff DESC