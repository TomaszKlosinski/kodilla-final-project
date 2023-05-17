Feature: user login
  Users want to be able to log in

  Background: login form is open
    Given user navigated to /login

  Scenario: user can login
    Given user "admin" exists
    When fill login form for user "admin"
    Then login succeeds without errors
