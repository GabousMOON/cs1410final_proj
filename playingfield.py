import pandas as pd
import numpy as np
import random as rd
from typing import List, Dict, Union
from enum import Enum
from pathogen import *
from places import Places
from historicalData import PopulationData, PathogenData

class PlayingField():
    def __init__(self) -> None:
        self.population: List[Person] = []
        self.pathogen: Pathogen = Pathogen()
        self.healthy_people_count:int = 0
        self.asymp_people_count:int = 0
        self.symp_people_count:int = 0
        self.kills = 0
        self.day_counter = 0
        self.places = Places()
        self.hist_pop_data = PopulationData()
        self.hist_path_data = PathogenData()

    def __str__(self) -> str:
        return f"Total Population: {len(self.population)}\nHealthy Population: {self.healthy_people_count}\n Asymptomatic Population: {self.asymp_people_count}\n Symptomatic Population: {self.symp_people_count}\nDay: {self.day_counter}\n Kills: {self.kills}"

    def populate(self, healthy_people:int, asymp_people:int, symp_people:int):
        for _ in range(healthy_people):
            self.population.append(Person())
        for _ in range(asymp_people):
            self.population.append(Person(infection_status = Health_Status.ASYMPTOMATIC))
        for _ in range(symp_people):
            self.population.append(Person(infection_status= Health_Status.SYMPTOMATIC))

        self.healthy_people_count = healthy_people
        self.asymp_people_count = asymp_people
        self.symp_people_count = symp_people

    def add_pathogen(self, type:Baddy, name:str ='', damage_factor:int = 1,
                    cure_defense:int = 0, longevity_factor:int =5, incubation_len:int =2,
                    symptomatic_infectability:int = 10, asymptomatic_infectability:int = 5, surface_infect_factor: float = 10):
        self.pathogen = Pathogen(type, name, damage_factor,
                                cure_defense, longevity_factor, incubation_len, symptomatic_infectability, asymptomatic_infectability, surface_infect_factor)

    def find_places_infection_value(self):
        for key, value in self.places.places.items():
            self.places.places[key][3] = round(np.average(value[:-1], weights = [0, 1, 3])/self.pathogen.surface_infect_factor, 2)

    def update(self):
        '''
        Updates everything
            Historical data
            Current Data
            Personal Data
            Pathogen Data
        '''
        new_historical_data_population = {
            "Healthy": self.healthy_people_count,
            "Asymptomatic": self.asymp_people_count,
            "Symptomatic": self.symp_people_count
        }
        for key in self.hist_pop_data.data.keys():
            self.hist_pop_data.data[key].append(new_historical_data_population[key])

        new_historical_data_pathogen = {
            'Damage Factor': self.pathogen.damage_factor,
            'Cure Defense': self.pathogen.cure_defense,
            'Longevity Factor': self.pathogen.longevity_factor,
            'Incubation Length': self.pathogen.incubation_len,
            'Symp. Infectability': self.pathogen.symptomatic_infectability,
            'Asymp. Infectability': self.pathogen.asymptomatic_infectability,
            'Surf. Infect. Factor': self.pathogen.surface_infect_factor
        }
        for key in self.hist_path_data.data.keys():
            self.hist_path_data.data[key].append(new_historical_data_pathogen[key])

        if self.day_counter >= 1:
            for person in self.population:
                person.check_for_infection(self)
            self.find_places_infection_value()

        self.healthy_people_count = len(list(person for person in self.population if person.infection_status == Health_Status.HEALTHY))
        self.asymp_people_count = len(list(person for person in self.population if person.infection_status == Health_Status.ASYMPTOMATIC))
        self.symp_people_count = len(list(person for person in self.population if person.infection_status == Health_Status.SYMPTOMATIC))

        self.day_counter += 1

field = PlayingField()

class Regen(Enum):
    LEVEL_5 = 25
    LEVEL_4 = 20
    LEVEL_3 = 15
    LEVEL_2 = 10
    LEVEL_1 = 5
    DEAD = 0

class Contractability(Enum):
    NORMAL = 50
    HIGH_RISK = 30
    HIGHEST_RISK = 10


class Health_Status(Enum):
    HEALTHY = 0
    ASYMPTOMATIC = 1
    SYMPTOMATIC = 2


class Person:
    def __init__(self, health: float = 100, age: int = 20, infection_status: Health_Status = Health_Status.HEALTHY,regeneration: Regen = Regen.LEVEL_3, social_factor: int = 15, fight_back_power: float = 1,immunocompromised: bool = False, errands: int = 0) -> None:
        self.health = health
        self.age = age
        self.infection_status = infection_status
        self.regeneration = regeneration
        self.social_factor = social_factor
        self.fight_back_power = fight_back_power
        self.immunocomped: bool = immunocompromised
        self.contract_risk: Contractability = Contractability.NORMAL
        self.errands: int = errands
        self.errands_list: List = []
        self.days_asymp: int = 0
        self.days_symp: int = 0
        self.contact_list:List['Person'] = []

    def __str__(self) -> str:
        return f"Person Object, health:{self.health}, age:{self.age}, infection_status:{self.infection_status.name}, regeneration:{Regen(self.regeneration).name}, talked to {len(self.contact_list)} other people today"

    def __repr__(self) -> str:
        return f"Person Object, health:{self.health}, age:{self.age}, infection_status:{self.infection_status.name}, regeneration:{Regen(self.regeneration).name}"

    def find_people_contacts(self, possibles: List['Person']) -> None:
        '''Builds a list of all the people seen that day'''
        new_contacts = []
        for _ in range(self.social_factor):
            new_contacts.append(rd.choice(possibles))
        self.contact_list = new_contacts

    def find_places(self, player_field = field) -> None:
        '''Builds a list of all the places gone that day'''
        errand_available = list(player_field.places.places.keys())
        for _ in range(self.errands):
            place = rd.choice(errand_available)
            self.errands_list.append(place)
        for place in self.errands_list:
            player_field.places.places[place][self.infection_status.value] += 1

    def find_infection_risk(self) -> None:
        '''Assigns an infection risk for the person'''
        if self.age < 5 or self.age > 70:
            self.contract_risk = Contractability.HIGH_RISK
            self.fight_back_power  = 1.5
            if self.immunocomped:
                self.contract_risk = Contractability.HIGHEST_RISK
                self.fight_back_power = 2

        elif self.immunocomped:
            self.contract_risk = Contractability.HIGH_RISK
            self.fight_back_power = 1.5

    def check_for_infection(self, playing_field = field):
        '''Does the bulk of updating the person for each day.'''

        # Checking for the transition between healthy - asymptomatic
        if self.infection_status == Health_Status.HEALTHY:
            self.find_places()
            self.find_people_contacts(playing_field.population)
            self.find_infection_risk()
            infection_points = 0
            # Going over the people
            for person in self.contact_list:
                if person.infection_status == Health_Status.ASYMPTOMATIC:
                    infection_points += field.pathogen.asymptomatic_infectability
                elif person.infection_status == Health_Status.SYMPTOMATIC:
                    infection_points += field.pathogen.symptomatic_infectability
            # Going over the Errands
            for place in self.errands_list:
                infection_points += playing_field.places.places[place][3]

            # Assessing if transition from healthy to asymptomatic is true
            if infection_points >= self.contract_risk.value:
                self.infection_status = Health_Status.ASYMPTOMATIC
            elif self.health < 100 and self.infection_status == Health_Status.HEALTHY:
                self.health += self.regeneration.value
                if self.health >= 100 and self.infection_status == Health_Status.HEALTHY:
                    self.health = 100

        # Checking transition from asymp-symptomatic
        elif self.infection_status == Health_Status.ASYMPTOMATIC:
            self.days_asymp += 1
            if self.days_asymp >= playing_field.pathogen.incubation_len:
                self.infection_status = Health_Status.SYMPTOMATIC
                self.days_asymp = 0

        # Chcking transition from symptomatic-healthy
        elif self.infection_status == Health_Status.SYMPTOMATIC:
            self.days_symp += 1
            self.health -= self.fight_back_power*field.pathogen.damage_factor
            if self.days_symp >= playing_field.pathogen.longevity_factor:
                self.infection_status = Health_Status.HEALTHY
                self.days_symp = 0

        # Clearing Daily information
        self.contact_list=[]
        self.errands_list = []





