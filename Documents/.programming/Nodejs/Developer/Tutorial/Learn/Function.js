#!/usr/bin/node

// Normal Function

//// Without Parmaters
function hello1(){
    console.log("Hello, World");
}

//// With Parmaters
function hello2(user){
    console.log(`Hello ${user}`);
}


// Return Function

//// Without Parmaters
function sum1(){
    return 1 + 1
}

//// With Parmaters
function sum2(x, y){
    return x + y
}


// Function Inside Function
function calculator(){
    function addition(x, y){
        return x + y
    }
    function subtract(x, y){
        return x - y
    }
    function multiple(x, y){
        return x * y
    }
    function division(x, y){
        return x / y
    }
    return addition
}


// Call Function
hello1()
hello2('SALAH')

console.log(sum1())
console.log(sum2(1, 1))

add = calculator()(1, 1)
console.log(`${add}`)
