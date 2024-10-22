WITH countrywise_profits as
                        (
                        SELECT airline_country, sum(profit) as total_profit
                        from `airline-438510.airlines.airlines`
                        GROUP BY airline_country
                        ),
            countrywise_flights as 
                        (
                        SELECT airline_country, count (distinct airline_id) as no_of_flights
                        from `airline-438510.airlines.airlines`
                        GROUP BY airline_country
                        )
        SELECT countrywise_profits.airline_country, countrywise_flights.no_of_flights, countrywise_profits.total_profit
        from countrywise_profits
                join countrywise_flights on countrywise_profits.airline_country = countrywise_flights.airline_country
