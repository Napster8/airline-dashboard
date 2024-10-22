--  Market share = (Total Revenue by Airline / Total Revenue) * 100

SELECT airline_name,
         ROUND(SUM(total_revenue) / (SELECT SUM(total_revenue) FROM `airline-438510.airlines.airlines`) * 100, 2) as market_share
FROM `airline-438510.airlines.airlines`
GROUP BY airline_name
ORDER BY market_share DESC