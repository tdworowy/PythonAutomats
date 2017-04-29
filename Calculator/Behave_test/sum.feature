Feature: sumFeature
    Scenario Outline : SumScenario
    Given Add <'numbers'> <'result'>

    Examples: Numbers
        |'numbers'|'result'|
        |100,100|200|
        |0,0|0|
        |99,1|100|
        |999,0|999|
        |0,9999|9999|