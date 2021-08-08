function fizzbuzz(num){
    if (num == 1){
         return"1"
    }
    else if (num == 2){
         return"2"
    }
    else if (num == 3){
         return"Fizz"
    }
    else if (num == 5){
         return"Buzz"
    }
    else if (num % 5 == 0 && num % 3 == 0){
         return"FizzBuzz"
    }
    else if (num % 3 == 0){
         return"Fizz"
    }
    else if (num % 5 == 0){
         return"Buzz"
    }
    else{
        return""
    }
}
module.exports = fizzbuzz