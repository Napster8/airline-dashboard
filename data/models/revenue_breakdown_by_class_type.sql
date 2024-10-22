SELECT class_type, 
        sum(total_revenue) / COUNT(*) as avg_revenue_per_flight, 
        sum(total_revenue) / SUM(number_of_passengers) as avg_revenue_per_passenger
FROM `airline-438510.airlines.airlines`
GROUP BY class_type
ORDER BY avg_revenue_per_flight DESC
