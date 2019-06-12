class Vehicle():

    def __init__(self,steering_mechanism,number_of_tyres):
        self.steering_mechanism = steering_mechanism
        self.min_number_of_tyres = min_number_of_tyres

    def set_min_number_of_tyres(min_number_of_tyres):
        self.min_number_of_tyres = min_number_of_tyres

    def get_min_number_of_tyres(self):
        return self.min_number_of_tyres

    def set_steering_mechanism(min_steering_mechanism):
        self.steering_mechanism = steering_mechanism

    def get_steering_mechanism(self):
        return self.steering_mechanism
