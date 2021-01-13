Feature: Converting numbers to roman

  Scenario: 1 is roman I
    Given 1 is given
    Then the output is I


  Scenario: 49 is roman XLIX
    Given 49 is given
    Then the output is XLIX


  Scenario: 575 is roman DLXXV
    Given 575 is given
    Then the output is DLXXV


  Scenario: 1024 is roman MXXIV
    Given 1024 is given
    Then the output is MXXIV

  Scenario: abc is error
    Given abc is given
    Then the output is error