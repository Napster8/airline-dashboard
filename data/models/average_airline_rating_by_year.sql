WITH airline_ratings AS (
    SELECT *
    FROM (
        SELECT 
            airline_name, 
            EXTRACT(YEAR FROM flight_date) AS year,
            ROUND(AVG(airline_rating), 2) AS avg_airline_rating
        FROM `airline-438510.airlines.airlines`
        GROUP BY airline_name, year
    )
    PIVOT (
        AVG(avg_airline_rating) FOR year IN (2021, 2022, 2023)
    )
    ORDER BY _2021 DESC, _2022 DESC, _2023 DESC
)
SELECT *,
       CASE 
            WHEN _2021 > _2022 AND _2021 > _2023 THEN "Decreasing Trend"
            WHEN _2023 > _2022 AND _2023 > _2021 THEN "Increasing Trend"
            ELSE "No Trend"
       END AS trend
FROM airline_ratings
ORDER BY trend