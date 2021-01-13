from src.Planet import Planet
from behave import *
from assertpy import *
from unittest import *

#Scenario 1
@given("2134835688 and Mercury are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 2134835688
    context.planet_name = "Merkury"

@then("the output is 280.88")
def step_imp(context):
    context.years = context.planet_class.count_age_on_planet(context.age_seconds,
                                                context.planet_name)
    assert_that(context.years).is_equal_to(280.88)


#Scenario 2
@given("1bln and Venus are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 1000000000
    context.planet_name = "Wenus"

@then("the output is 51.51")
def step_imp(context):
    context.years = context.planet_class.count_age_on_planet(context.age_seconds,
                                                context.planet_name)
    assert_that(context.years).is_equal_to(51.51)

# Scenario 3
@given("1bln and Earth are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 1000000000
    context.planet_name = "Ziemia"

@then("the output is 31.69")
def step_imp(context):
    context.years = context.planet_class.count_age_on_planet(context.age_seconds,
                                                             context.planet_name)
    assert_that(context.years).is_equal_to(31.69)



# Scenario 4
@given("1bln and Mars are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 1000000000
    context.planet_name = "Mars"

@then("the output is 16.85")
def step_imp(context):
    context.years = context.planet_class.count_age_on_planet(context.age_seconds,
                                                             context.planet_name)
    assert_that(context.years).is_equal_to(16.85)


# Scenario 5
@given("1bln and Jupiter are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 1000000000
    context.planet_name = "Jowisz"

@then("the output is 2.67")
def step_imp(context):
    context.years = context.planet_class.count_age_on_planet(context.age_seconds,
                                                             context.planet_name)
    assert_that(context.years).is_equal_to(2.67)

# Scenario 6
@given("2134835688 and Mercur are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 2134835688
    context.planet_name = "Merkur"

@then("function returns ValueError")
def step_imp(context):
    assert_that(context.planet_class.count_age_on_planet)\
        .raises(ValueError).when_called_with(context.age_seconds,
                                             context.planet_name)

# Scenario 7
@given("abc and Mercury are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = "abc"
    context.planet_name = "Merkury"

# Scenario 8
@given("0 and Mercury are given")
def step_imp(context):
    context.planet_class = Planet()
    context.age_seconds = 0
    context.planet_name = "Merkury"




