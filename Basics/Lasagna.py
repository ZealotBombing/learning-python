#an exercice from Exercism.com


class Lasagna_Exercise:
    
    def bake_time_remaining(self, current_time):
        """"""
        EXPECTED_BAKE_TIME = 40
        return EXPECTED_BAKE_TIME - current_time
        
    def preparation_time_in_minutes(self, number_of_layers):
        """"""
        EXPECTED_BAKE_TIME = 40
        return number_of_layers * 2


    def elapsed_time_in_minutes(self, number_of_layers, elapsed_bake_time ):
        """"""
        EXPECTED_BAKE_TIME = 40
        return elapsed_bake_time + self.preparation_time_in_minutes(number_of_layers)