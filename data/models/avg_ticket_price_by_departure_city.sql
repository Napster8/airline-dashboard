SELECT departure_city, 
        ROUND(AVG(ticket_price), 2) as avg_ticket_price
FROM `airline-438510.airlines.airlines`
GROUP BY departure_city
ORDER BY avg_ticket_price DESC