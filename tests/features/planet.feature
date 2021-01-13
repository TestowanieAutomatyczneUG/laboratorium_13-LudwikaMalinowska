Feature: Calculating year on planet

  Scenario: 1 earth year on Mercury is 280.88 years
    Given 2134835688 and Mercury are given
    Then the output is 280.88

  Scenario: 1bln seconds on Venus is 51.51 years
    Given 1bln and Venus are given
    Then the output is 51.51

  Scenario: 1bln seconds on Earth is 31.69 years
    Given 1bln and Earth are given
    Then the output is 31.69

  Scenario: 1bln seconds on Mars is 16.85 years
    Given 1bln and Mars are given
    Then the output is 16.85

  Scenario: 1bln seconds on Jupiter is 2.67 years
    Given 1bln and Jupiter are given
    Then the output is 2.67




  Scenario: 1 earth year on Mercur is error
    Given 2134835688 and Mercur are given
    Then function returns ValueError

  Scenario: abc on Mercury is error
    Given abc and Mercury are given
    Then function returns ValueError

  Scenario: 0 on Mercury is error
    Given 0 and Mercury are given
    Then function returns ValueError