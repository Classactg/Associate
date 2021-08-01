import unittest
from supermarket import Checkout


class TestCheckout(unittest.TestCase):
    def test_fizz(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            print(cart)
            assert cart 
    def test1(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            cart.addItem(["green apple"])
            assert cart.listItems == [["green apple"]]
    def test2(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            # cart.addItem(["green apple"])
            cart.addPrice(["green apple"], 0.45)
            print(cart.listItems)
            assert cart.listItems == [["green apple",0.45]]
    def test3(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            # cart.addItem(["green apple"])
            cart.addPrice(["green apple"], 0.45) #can add multiple items
            print(cart.listItems) 
            cart.calculator()
            assert cart.currentValue == 0.9 #can calculate totals from the price of multiple items
    def test4(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            # cart.addItem(["green apple"])
            cart.addDiscount(["green apple"], 0.45, 0.05)
            print(cart.listItems)
            assert cart.listItems == [['green apple', 0.45], ['green apple', 0.45], ['green apple', 0.45, 0.05]]
    def test5(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            cart.calculator()
            print(cart.currentValue)
            assert cart.currentValue == 0.9225
    def test6(self):
        # for i in [3, 6, 9, 18]:
        #     print('testing', i)
            cart = Checkout()
            cart.addItem(["honey crisp apple"])
            cart.calculator()
            print(cart.listItems)
            assert cart.currentValue == 0.9225
    
# TestCheckout.test_fizz()
test = TestCheckout()
print(test.test_fizz())
print(test.test1())
print(test.test2())
print(test.test3())
print(test.test4())
print(test.test5())
print(test.test6())
