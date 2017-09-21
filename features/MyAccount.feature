Feature: Verify My Account

  Scenario: Validate My Account Page
    Given I have my sky account subscription details page
    When I check for page elements
    Then the page elements are displayed
