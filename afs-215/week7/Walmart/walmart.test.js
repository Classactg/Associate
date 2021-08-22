const expect = require('chai').expect;
const {Checkout} = require ("./supermarket.js")
console.log(Checkout)
// var a = "1"

describe('Checkout test', function(){

    it('Can create an instance of the Checkout class.', function(){
        const expected = "object";
const actual = typeof new Checkout();

expect(actual).to.deep.equal(expected)

    })
    it('Can add an item.', function(){
        const expected = 1
        var instance = new Checkout()
        instance.addItem("large eggs")
const actual = instance.listItems.length;

expect(actual).to.deep.equal(expected)

    })
    it('Can add an item price.', function(){
        const expected = 5
        var instance = new Checkout()
        instance.addItem("large eggs", 5)
const actual = instance.listItems [0].price;

expect(actual).to.deep.equal(expected)

    })
    it('Can calculate the current total.', function(){
        const expected = 8
        var instance = new Checkout()
        instance.addItem("large eggs", 5)
        instance.addItem("milk", 3)
const actual = instance.calculator();

expect(actual).to.deep.equal(expected)

    })
    it('Can add multiple items and get correct total.', function(){
        const expected = 9
var instance = new Checkout()
instance.addItem("large eggs", 5)
instance.addItem("milk", 3)
instance.addItem("apple", 1)
const actual = instance.calculator();

expect(actual).to.deep.equal(expected)

    })
    it('Can add discount rules.', function(){
        const expected = 12.2
        var instance = new Checkout()
instance.addItem("large eggs", 5, 0.5)
instance.addItem("milk", 3, 0.2)
instance.addItem("apple", 1, 0.1)
const actual = instance.calculator();


expect(actual).to.deep.equal(expected)

    })    
    it('Can apply discount rules to the total.', function(){
        const expected = 12.2

        var instance = new Checkout()
        instance.addItem("large eggs", 5, 0.5)
        instance.addItem("milk", 3, 0.2)
        instance.addItem("apple", 1, 0.1)
        const actual = instance.calculator();
        

expect(actual).to.deep.equal(expected)

    })
    it('Exception is thrown for item added without a price.', function(){
        var instance = new Checkout()
        const expected = "one of the items doesn't have a price";
        instance.addItem("large eggs", 5, 0.5)
        instance.addItem("milk")
        instance.addItem("apple", 1, 0.1)
        const actual = instance.calculator();


expect(actual).to.deep.equal(expected)

    })
}
)