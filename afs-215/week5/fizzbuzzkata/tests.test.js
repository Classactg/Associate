const expect = require('chai').expect;
const fizzbuzz = require ("./Fizzbuzzkata")
console.log(fizzbuzz)
// var a = "1"

describe('fizzbuzz test', function(){

    it('check the dish has valid name.', function(){
        const expected = "function";
const actual = typeof fizzbuzz;

expect(actual).to.deep.equal(expected)

    })
    it('Get "1" when I pass in 1.', function(){
        const expected = "1";
const actual =  fizzbuzz(1);

expect(actual).to.deep.equal(expected)

    })
    it('Get "2" when I pass in 2.', function(){
        const expected = "2";
const actual =  fizzbuzz(2);

expect(actual).to.deep.equal(expected)

    })
    // Here starts week 6.
    it('Get "Fizz" when I pass in 3.', function(){
        const expected = "Fizz";
const actual =  fizzbuzz(3);

expect(actual).to.deep.equal(expected)

    })
    it('Get "Buzz" when I pass in 5.', function(){
        const expected = "Buzz";
const actual =  fizzbuzz(5);

expect(actual).to.deep.equal(expected)

    })
    it('Get "Fizz" when I pass in 6.', function(){
        const expected = "Fizz";
const actual =  fizzbuzz(6);

expect(actual).to.deep.equal(expected)

    })
    it('Get "Buzz" when I pass in 10.', function(){
        const expected = "Buzz";
const actual =  fizzbuzz(10);

expect(actual).to.deep.equal(expected)

    })
    it('Get "FizzBuzz" when I pass in 15.', function(){
        const expected = "FizzBuzz";
const actual =  fizzbuzz(15);

expect(actual).to.deep.equal(expected)

    })
}
)