Feature: Cat Fact API
    An API for facts about cats

    Scenario: Get random fact
        Given I send a GET request to fact
        Then The API returns response 200
        And The returned data is correct

    Scenario: Get random facts
        Given I send a GET request to facts
        Then The API returns response 200
        And The list of facts is returned

    Scenario: Get list of breeds
        Given I send a GET request to breeds
        Then The API returns response 200
        And The list of breeds is returned