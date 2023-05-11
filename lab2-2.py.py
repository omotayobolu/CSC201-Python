class Scooter:
    def __init__(self, name, starting_fee, price_per_100m, available_riding_distance_in_km):
        self.name = name #name of rental company
        self.starting_fee = starting_fee #starting fee for a ride
        self.price_per_100m = price_per_100m #price per 100m of riding
        self.available_riding_distance = available_riding_distance_in_km 

    def price(self, ride_length):
        self.ride_length = ride_length #length of ride in km
        if ride_length <= self.available_riding_distance:
            #to calculate the price of a ride    
            return  self.starting_fee + self.ride_length * self.price_per_100m * 10 
        else:
            return 1000             

    # takes the lenggth of the ride as an argument and subtract it from the available_riding_distance
    def ride(self, ride_length):
        self.ride_length = ride_length
        distance = self.available_riding_distance - ride_length
        if(distance < 0):            
            distance = 0

    def charge(self, distance):
        self.distance = self.available_riding_distance + distance #in kilometers


class Rental:
    def __init__(self, scooters):
        self.scooters = scooters

    def display_choices(self, length_of_ride):
            # prints the name of each scooter and price of the ride, will also order the 
            # scooters from top to bottom, starting with the cheapest. use the price method to
            # find the price of the ride
             
            choices = []
            for scooter in self.scooters:
                price = scooter.price(length_of_ride)
                if price!= 1000:
                    choices.append((scooter.name, price))
                    choices.sort(key=lambda x : x[1])
                    for name, price in choices:
                        print (f"{name}: {price} naira")


    def rent(self, name_of_scooter, length_of_ride):
        for scooter in self.scooters:
            if scooter.name == name_of_scooter:
                price = scooter.price(length_of_ride)
                if price != 1000:
                    print(f"Riding {name_of_scooter} for {length_of_ride} km costs {price} naira.")
                    scooter.ride(length_of_ride)
                else:
                    print(f"{name_of_scooter} does not have enough available distance for {length_of_ride} km ride")
                return
            print(f"{name_of_scooter} is not in our rental list")                        

    def charge_scooter(self, scooter_to_charge, no_of_km):
        for scooter in self.scooters:
            if scooter.name == scooter_to_charge:
                scooter.charge(no_of_km)
                print(f"Charged {scooter_to_charge} with {no_of_km} km")
                return
        print(f"{scooter_to_charge} is not in our rental list")

scooters = [
    Scooter("Bolt", 1.5, 0.1, 20),
    Scooter("Tuul", 1, 0.15, 18),
    Scooter("Bird", 0, 0.3, 34)
 ]                       

rental = Rental(scooters)
rental.display_choices(2)
rental.rent("Bolt", 3)
rental.rent("Tuul", 18)
rental.rent("Tuul", 5)
rental.charge_scooter("Tuul", 5)
rental.rent("Tuul", 2)