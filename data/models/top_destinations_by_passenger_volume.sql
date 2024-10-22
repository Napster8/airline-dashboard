SELECT arrival_city as destination, 
        COUNT(*) as passenger_volume
from `airline-438510.airlines.airlines`
GROUP BY destination
ORDER BY passenger_volume DESC