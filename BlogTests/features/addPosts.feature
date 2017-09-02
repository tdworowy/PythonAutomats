Feature: Scientific Calculator2
    Scenario Outline: Sum scenario
     Given open login page
     Then login page is opened
     When login admin
     Then admin page is opened
     When add Post <title> <body>

    Examples: posts
    | title          | body |
    | test1      | test test    |
    | test2          | test      |
    | łęśćę          | test     |
    | test3         | łęśćę    |
    | t e s t 4        | test    |
    | !@#$%^^&&(*       | !@#$%^^&&(*   |