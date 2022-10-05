Feature: Get Coffee

    Scenario: Get Coffee Image
        Given I send a GET request to Coffee image
        Then The API returns response 200
        And The returned image is correct

    Scenario: Get Coffee Image JSON
        Given I send a GET request to Coffee JSON
        Then The API returns response 200
        And The returned JSON is correct