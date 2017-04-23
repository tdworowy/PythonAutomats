Feature: Scientific Calculator
    Scenario: Open Scientific Calculator
    Given open scientific calculator
    Then check calculator
    Then tear down

    Scenario: sum 2 + 2 = 4
    Given open scientific calculator
    And sum 2 + 2
    Then check result

    Scenario: sum -2 + 2 = 0
    Given open scientific calculator
    And sum -2 + 2
    Then check result


    Scenario: sum 1000 + 1000 = 2000
    Given open scientific calculator
    And sum -2 + 2
    Then check result
