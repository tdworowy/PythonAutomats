Feature: Scientific Calculator2
# feature is sipped , WHY !!!
    Scenario Outline : parametrized sum
        Given open scientific calculator
        When sum <first> <second>
        Then check result

        Examples: Numbers
        | first     | second|
        | 100       | 100   |
        | 0         | 0     |
        | 99        | 1     |
        | 999       | 0     |
        | 0         | 9999  |