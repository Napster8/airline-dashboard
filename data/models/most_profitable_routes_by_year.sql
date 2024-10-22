WITH profits as (
SELECT departure_city,
        arrival_city,
        EXTRACT(YEAR FROM flight_date) as year,
        SUM(profit) AS profit
FROM `airline-438510.airlines.airlines`
GROUP BY departure_city, arrival_city, year
),
max_profit as (
            SELECT year, MAX(profit) as max_profit
            FROM profits
            GROUP BY year
)
SELECT p.departure_city, p.arrival_city, p.year, p.profit
FROM profits p
JOIN max_profit mp ON p.year = mp.year AND p.profit = mp.max_profit
ORDER BY p.year ASC
