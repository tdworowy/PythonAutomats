Feature: AddPost
    Scenario Outline: Add post scenario
     Given user is logged as Admin
     When user adds Post <title> <body>
     Then post is displayed on main page
    Examples: posts
    | title          | body          |
    | test1          | test test     |
    | test2          | test          |
    | łęśćę          | test          |
    | test3          | łęśćę         |
    | t e s t 4      | test          |
    | !@#$%^^&&(*    | !@#$%^^&&(*   |
    | 1              | 1             |