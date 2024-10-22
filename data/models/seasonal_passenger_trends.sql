WITH seasonal_passenger_trends as (
SELECT EXTRACT(MONTH FROM flight_date) as month,
        COUNT(*) as number_of_passengers
FROM `airline-438510.airlines.airlines`
GROUP BY month
ORDER BY month
)
SELECT *,
        CASE WHEN month IN (12, 1, 2) THEN "Winter"
                WHEN month IN (3, 4, 5) THEN "Spring"
                WHEN month IN (6, 7, 8) THEN "Summer"
                ELSE "Fall"
        END as season
          FROM seasonal_passenger_trends