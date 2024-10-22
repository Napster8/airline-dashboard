SELECT class_type, 
        ROUND ( avg( ( (total_revenue - costs) / total_revenue) * 100 ), 2) as average_profit_margin
FROM `airline-438510.airlines.airlines`
GROUP BY class_type
ORDER BY average_profit_margin DESC
