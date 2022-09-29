Feature: Cat Fact API
    An API for facts about cats

    Scenario: Get random fact
        When I send a GET request to fact
        Then the API returns reponse 200

    Scenario: Get random facts
        When I send a GET request to facts
        Then the API returns reponse 200

    Scenario: Get list of breeds
        When I send a GET request to breeds
        Then the API returns reponse 200