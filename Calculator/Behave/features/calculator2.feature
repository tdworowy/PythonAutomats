Feature: Scientific Calculator2
# feature is sipped , WHY !!!
    Scenario Outline : Sum scenario <sum>
    Given open scientific calculator
    When sum <sum>
    Then check <result>

    Examples: Numbers
        | sum      | result|
        | 100,100  | 200   |
        | 0,0      | 0     |
        | 99,1     | 100   |
        | 999,0    | 999   |
        | 0,9999   | 9999  |