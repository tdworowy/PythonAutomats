Feature: Scientific Calculator1
    Scenario: Open Scientific Calculator
    Given open scientific calculator
    Then check calculator

    Scenario: sum 2 + 2 = 4
    Given open scientific calculator
    When sum 2 + 2
    Then check result

    Scenario: sum -2 + 2 = 0
    Given open scientific calculator
    When sum -2 + 2
    Then check result


    Scenario: sum 1000 + 1000 = 2000
    Given open scientific calculator
    When sum -2 + 2
    Then check result

