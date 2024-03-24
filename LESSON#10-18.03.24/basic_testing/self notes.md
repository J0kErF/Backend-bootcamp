the type of testing I did in test_raffle.py is to validate that the logical implementation is working not the edge cases.
I tried to make it as pro as I can by adding a config_tests.py file that contains fixture (basicly init the object to start by validating that the constructor works propaply).

the tests I have provided validates the constructor, add_person and buy_tickets logical implementation the last function I don't really how to test it from this side in this test unit (test file).
I think I should test the function That I call and thats it because I just call it and returns immediatly tha value like a bridge.

the next step is to do the same validation for utils.py and then I will go throw testing the error handling.

I am thinking about automating all the tests maybe with each push to github using github actions.