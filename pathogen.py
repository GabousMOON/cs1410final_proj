from enum import Enum
from typing import List, Dict


class Baddy(Enum):
    UNSET = "No pathogen"
    VIRUS = 'Virus'
    BACTERIA = 'Bacteria'
    PROTAZOA = "Protazoa"
    PRION = "Prion"
    FUNGUS = "Fungus"


class Pathogen:
    def __init__(self, type: Baddy = Baddy.UNSET, name: str = 'pathogen', damage_factor: int = 5, cure_defense: int = 0, longevity_factor: int = 5, incubation_len: int = 5, symptomatic_infectability: int = 10, asymptomatic_infectability: int = 5, surface_infect_factor: float = 10) -> None:
        self.type = type
        self.name: str = name
        self.damage_factor: int = damage_factor
        self.cure_defense: int = cure_defense
        self.longevity_factor: int = longevity_factor
        self.incubation_len: int = incubation_len
        self.symptomatic_infectability: int = symptomatic_infectability
        self.asymptomatic_infectability: int = asymptomatic_infectability
        self.surface_infect_factor = surface_infect_factor


    def __str__(self) -> str:
        return f"Pathogen type: {self.type}, name: {self.name}, damage factor: {self.damage_factor}, cure defense{self.cure_defense}, longevity: {self.longevity_factor}"

    def __repr__(self) -> str:
        return f"Pathogen(type: {self.type}, name:{self.name}, damage_factor: {self.damage_factor}, cure_defenese{self.cure_defense}, longevity: {self.longevity_factor}, incubation_len: {self.incubation_len}, symptomatic_infectability: {self.symptomatic_infectability}, asymptomatic_infectability: {self.asymptomatic_infectability}, surface_infect_factor: {self.surface_infect_factor})"

    def upgrade_damage_factor(self, amount: int) -> None:
        self.damage_factor += amount

    def upgrade_cure_defense(self, amount: int) -> None:
        self.cure_defense += amount

    def upgrade_longevity_factor(self, amount: int) -> None:
        self.longevity_factor = amount

    def upgrade_incubation(self, amount: int) -> None:
        self.incubation_len += amount

    def upgrade_sympto_infectability(self, amount: int) -> None:
        self.symptomatic_infectability += amount

    def upgrade_asympto_infectability(self, amount: int) -> None:
        self.asymptomatic_infectability += amount

    def upgrade_surface_infect_factor(self, amount: float) -> None:
        '''
            amount: decreases the surface_infect_factor by that amount
            Decreases allow for higher points on the place[3] (see places)
        '''
        self.surface_infect_factor -= amount

