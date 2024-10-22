SELECT departure_city, 
        arrival_city, 
        flight_duration, 
        AVG(ticket_price) as avg_ticket_price
FROM `airline-438510.airlines.airlines`
GROUP BY departure_city, arrival_city, flight_duration
ORDER BY flight_duration DESC, avg_ticket_price DESC