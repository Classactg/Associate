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
}
)