Feature: Scientific Calculator
    Scenario: Open Scientific Calculator
    Given  Set up
    When open calculator
    then check calculator
    then tear down

    Scenario: sum 2 + 2
    Given  Set up
    When open calculator
    and sum 2 + 2
    then check result
    then tear down