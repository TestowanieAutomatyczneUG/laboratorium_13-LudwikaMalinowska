from src.Roman import RomanNumerals
from behave import *
from assertpy import *
from unittest import *

#Scenario 1
@given("1 is given")
def step_imp(context):
    context.roman_class = RomanNumerals()
    context.decimalNumber = 1

@then("the output is I")
def step_imp(context):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to("I")


#Scenario 2
@given("49 is given")
def step_imp(context):
    context.roman_class = RomanNumerals()
    context.decimalNumber = 49

@then("the output is XLIX")
def step_imp(context):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to("XLIX")


#Scenario 3
@given("575 is given")
def step_imp(context):
    context.roman_class = RomanNumerals()
    context.decimalNumber = 575

@then("the output is DLXXV")
def step_imp(context):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to("DLXXV")


#Scenario 4
@given("1024 is given")
def step_imp(context):
    context.roman_class = RomanNumerals()
    context.decimalNumber = 1024

@then("the output is MXXIV")
def step_imp(context):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to("MXXIV")


#Scenario 5
@given("abc is given")
def step_imp(context):
    context.roman_class = RomanNumerals()
    context.decimalNumber = "abc"

@then("the output is error")
def step_imp(context):
    context.romanNumber = context.roman_class.roman(context.decimalNumber)
    assert_that(context.romanNumber).is_equal_to("Please enter correct number")

