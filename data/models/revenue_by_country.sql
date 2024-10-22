select airline_country, sum(total_revenue) as total_revenue
from `airline-438510.airlines.airlines`
group by airline_country
order by total_revenue desc