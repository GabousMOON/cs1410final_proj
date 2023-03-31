'''Testing for people'''
import pytest
from playingfield import *
from pathogen import *

def test_find_people_contacts():
    tester_field = PlayingField()
    subject = Person(social_factor=3)
    tester_field.add_pathogen(Baddy.BACTERIA, 'test_bact')

    tester_field.population = [
        Person(),
        Person(infection_status=Health_Status.ASYMPTOMATIC),
        Person(infection_status=Health_Status.SYMPTOMATIC),
        Person(health = 10),
        Person(health = 90)
    ]

    subject.find_people_contacts(tester_field.population)
    assert len(subject.contact_list) == 3

    sub_2 = Person(social_factor= 10)
    sub_2.find_people_contacts(tester_field.population)
    assert len(sub_2.contact_list) == 10

def test_find_infection_risk():
    average_subject = Person(age = 20)
    young_subject = Person(age= 3)
    old_subject = Person(age = 90)
    immunocomped_subject = Person(age = 20, immunocompromised = True)
    immunocomped_old = Person(age = 80, immunocompromised = True)
    immunocomped_young = Person(age = 3, immunocompromised = True)
    average_subject.find_infection_risk()
    young_subject.find_infection_risk()
    old_subject.find_infection_risk()
    immunocomped_old.find_infection_risk()
    immunocomped_subject.find_infection_risk()
    immunocomped_young.find_infection_risk()
    assert average_subject.contract_risk == Contractability.NORMAL
    assert young_subject.contract_risk == Contractability.HIGH_RISK
    assert old_subject.contract_risk == Contractability.HIGH_RISK
    assert immunocomped_subject.contract_risk == Contractability.HIGH_RISK
    assert immunocomped_old.contract_risk == Contractability.HIGHEST_RISK
    assert immunocomped_young.contract_risk == Contractability.HIGHEST_RISK

def test_find_places():
    tester_field = PlayingField()
    person = Person(errands=5)
    person.find_places(tester_field)
    assert len(person.errands_list) == 5
    assert sum(list(value[0] for value in tester_field.places.places.values())) == 5
    new_person = Person(errands = 10, infection_status=Health_Status.ASYMPTOMATIC)
    new_person.find_places(tester_field)
    assert len(new_person.errands_list) == 10
    assert sum(list(value[1] for value in tester_field.places.places.values())) == 10
    last_person = Person(errands = 15, infection_status=Health_Status.SYMPTOMATIC)
    last_person.find_places(tester_field)
    assert len(last_person.errands_list) == 15
    assert sum(list(value[2] for value in tester_field.places.places.values())) == 15

def test_check_for_infection_healthy():
    tester_field = PlayingField()
    subject = Person(age = 20)
    tester_field.populate(0, 50, 0)
    tester_field.add_pathogen(type = Baddy.VIRUS, name = "tester Virus")
    subject.check_for_infection(tester_field)
    assert subject.infection_status == Health_Status.ASYMPTOMATIC
    new_subject = Person(age = 20, social_factor=9)
    tester_field.populate(0, 10, 0)
    new_subject.check_for_infection(tester_field)
    assert new_subject.infection_status == Health_Status.HEALTHY

def test_check_for_infection_asymp():
    tester_field = PlayingField()
    subject = Person(age=20, infection_status=Health_Status.ASYMPTOMATIC)
    tester_field.add_pathogen(type=Baddy.BACTERIA, name = 'tester', damage_factor= 5, longevity_factor=2, incubation_len=2)
    assert subject.infection_status == Health_Status.ASYMPTOMATIC
    subject.check_for_infection(tester_field)
    assert subject.days_asymp == 1
    subject.check_for_infection(tester_field)
    assert subject.infection_status == Health_Status.SYMPTOMATIC
    assert subject.days_asymp == 0

def test_check_for_infection_symp():
    tester_field = PlayingField()
    subject = Person(age=20, infection_status=Health_Status.SYMPTOMATIC)
    tester_field.add_pathogen(type = Baddy.BACTERIA, name = 'tester', damage_factor = 5, longevity_factor=3)
    assert subject.days_symp == 0
    subject.check_for_infection(tester_field)
    assert subject.days_symp == 1
    assert subject.infection_status == Health_Status.SYMPTOMATIC
    assert subject.health == 95
    subject.check_for_infection(tester_field)
    assert subject.days_symp == 2
    assert subject.health == 90
    subject.check_for_infection(tester_field)
    assert subject.days_symp == 0
    assert subject.infection_status == Health_Status.HEALTHY
    assert subject.health == 85

def test_check_for_infection_recovery():
    tester_field = PlayingField()
    tester_field.populate(100, 0, 0)
    subject = Person(age = 20, health = 50)
    subject.check_for_infection(tester_field)
    assert subject.health == 65
    subject.check_for_infection(tester_field)
    assert subject.health == 80
    subject.check_for_infection(tester_field)
    assert subject.health == 95
    subject.check_for_infection(tester_field)
    assert subject.health == 100















