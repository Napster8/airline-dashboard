-- Pearson Co-Relation Formula: P = Cov(X, Y) / (σx * σy)
-- Cov(X, Y) = Σ((X - μx) * (Y - μy)) / n
-- where μx = mean of X, μy = mean of Y, n = number of observations

SELECT CORR(avg_airline_rating, avg_profit) AS pearson_correlation
FROM (
    SELECT 
        airline_name, 
        ROUND(AVG(airline_rating), 2) AS avg_airline_rating,
        ROUND(AVG(profit), 2) AS avg_profit
    FROM `airline-438510.airlines.airlines`
    GROUP BY airline_name
)
