import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(7) == ''
    def test1(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(1) == "1"
    def test2(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(2) == "2"
    def test3(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(3) == "Fizz"
    def test4(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(5) == "Buzz"
    def test5(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(6) == "Fizz"
    def test6(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(10) == "Buzz"
    def test7(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            assert fizzbuzz(15) == "FizzBuzz"
# TestFizzBuzz.test_fizz()
test = TestFizzBuzz()
print(test.test_fizz())
print(test.test1())
print(test.test2())
print(test.test3())
print(test.test4())
print(test.test5())
print(test.test6())
print(test.test7())