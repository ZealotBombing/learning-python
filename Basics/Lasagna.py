#an exercice from Exercism.com

EXPECTED_BAKE_TIME = 40

class Lasagna_Exercise:
    
    def bake_time_remaining(current_time):
        """"""
        return EXPECTED_BAKE_TIME - current_time
        
    def preparation_time_in_minutes(number_of_layers):
        """"""
        return number_of_layers * 2


    def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time ):
        """"""
        return elapsed_bake_time + self.preparation_time_in_minutes(number_of_layers)