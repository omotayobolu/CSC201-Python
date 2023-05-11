class Scooter:
    def __init__(self, name, starting_fee, price_per_100m, available_riding_distance_in_km):
        self.name = name #name of rental company
        self.starting_fee = starting_fee #starting fee for a ride
        self.price_per_100m = price_per_100m #price per 100m of riding
        self.available_riding_distance = available_riding_distance_in_km 

    def price(self, ride_length):
        self.ride_length = ride_length #length of ride in km
        if ride_length <= self.available_riding_distance:
            return self.price_per_100m * self.starting_fee   
        else:
            return 1000             

    def ride(self, ride_length):
        self.ride_length = ride_length
        if(self.available_riding_distance - ride_length < 0):
            distance = 0            

    def charge(self, no_of_km):
        self.no_of_km = self.available_riding_distance + no_of_km
