'''Testing all of the functions of the playing field'''

import pytest
from playingfield import *
from pathogen import *

def test_populate_function():
    tester_field = PlayingField()
    tester_field.populate(100, 20, 10)
    assert len(tester_field.population) == 130
    assert tester_field.healthy_people_count == 100
    assert tester_field.asymp_people_count == 20
    assert tester_field.symp_people_count == 10
    assert tester_field.day_counter == 0

def test_add_pathogen_function():
    tester_field = PlayingField()
    tester_field.add_pathogen(Baddy.BACTERIA, name = 'tester bact', damage_factor= 10)
    assert tester_field.pathogen.type == Baddy.BACTERIA
    assert tester_field.pathogen.name == 'tester bact'
    assert tester_field.pathogen.damage_factor == 10
    assert tester_field.pathogen.cure_defense == 0

def test_find_places_infection_values():
    tester_field = PlayingField()
    tester_field.places.places = {
        "BANK": [0, 0, 0, 0],
        'SCHOOL':[100, 0, 0, 0],
        'POST_OFFICE':[0, 0, 40, 0],
        'GROCERY_STORE':[0, 20, 0, 0],
        'GYM': [100, 10, 30, 0]
    }
    tester_field.add_pathogen(type=Baddy.BACTERIA, name = 'tester bacteria', damage_factor=0)
    tester_field.find_places_infection_value()
    assert tester_field.places.places['BANK'][3] == 0
    assert tester_field.places.places['SCHOOL'][3] == 0
    assert tester_field.places.places['POST_OFFICE'][3] == 3
    assert tester_field.places.places['GROCERY_STORE'][3] == .5
    assert tester_field.places.places['GYM'][3] == 2.5


def test_update_everything_no_sick_people():
    test_field = PlayingField()
    test_field.populate(100, 0, 0)
    test_field.add_pathogen(type=Baddy.BACTERIA, name = "Bro", damage_factor = 1, longevity_factor=5, incubation_len=5)
    test_field.update()
    assert test_field.day_counter == 1
    assert len(test_field.population) == 100
    assert len(test_field.hist_pop_data.data['Healthy']) == 1
    assert test_field.hist_pop_data.data['Healthy'][0] == 100

def test_update_everything_start_only_asymp():
    test_field = PlayingField()
    test_field.populate(0, 10, 0)
    test_field.add_pathogen(type=Baddy.BACTERIA, name = 'test pathogen', damage_factor= 10, longevity_factor= 3, incubation_len=2)

    test_field.update()
    assert test_field.day_counter == 1
    assert len(test_field.population) == 10
    for person in test_field.population:
        assert person.days_asymp == 0

    test_field.update()
    assert test_field.day_counter == 2
    assert len(test_field.population) == 10
    for person in test_field.population:
        assert person.days_asymp == 1

    test_field.update()
    assert test_field.day_counter == 3
    assert len(test_field.population) == 10
    for person in test_field.population:
        assert person.days_asymp == 0
        assert person.infection_status == Health_Status.SYMPTOMATIC

    for _ in range(4):
        test_field.update()

    assert test_field.day_counter == 7
    assert len(test_field.population) == 10
    for person in test_field.population:
        assert person.days_symp == 0
        assert person.days_asymp == 0
        assert person.infection_status == Health_Status.HEALTHY

def test_people_can_be_made_sick_update():
    test_field = PlayingField()
    test_field.populate(0, 0, 10)
    test_field.add_pathogen(type=Baddy.BACTERIA, name = 'test pathogen', damage_factor = 5, longevity_factor= 9, incubation_len=2, symptomatic_infectability=10)
    person = Person(age = 20, social_factor=20)
    test_field.population.append(person)
    for _ in range(2):
        test_field.update()

    assert test_field.asymp_people_count == 1
    assert test_field.symp_people_count == 10

    for _ in range(5):
        test_field.update()

    assert test_field.asymp_people_count == 0
    assert test_field.symp_people_count == 11
    for _ in range(4):
        test_field.update()

    assert test_field.symp_people_count == 1

    for _ in range(10):
        test_field.update()
    assert test_field.symp_people_count == 0
    assert test_field.healthy_people_count == 11









