'''
Places Module
Just a simple interface
key = Places
value[0] = Healthy people that visited that day
value[1] = Asymptomatic people that visited that day
value[2] = Symptomatic people that visited that day
value[3] = (1/4) * value[1] + (3/4) value[2] / pathogen.surface_infect_factor
    * this value will be what is added to a person's point total when evaluating if they are to make the transition from healthy to asymptomatic
'''

from typing import Dict, List
class Places:
    def __init__(self) -> None:
        self.places:Dict[str, List] = {
            "BANK":[0,0,0,0.0],
            "SCHOOL":[0,0,0,0.0],
            "POST_OFFICE" : [0,0,0,0.0],
            "GROCERY_STORE" : [0,0,0,0.0],
            "GYM" : [0,0,0,0.0]
        }
    def __str__(self) -> str:
        return f"{self.places}"

