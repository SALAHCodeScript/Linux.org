#!/usr/bin/node

// Without Initiailizing
class Welcome1{
    name = "SALAH";
    //// Method
    hello(name) {
        return `Hello ${name}`
    }
}
//// Create A New Class
// let user1 = new Welcome1;
// console.log(user1.name);
// console.log(user1.hello());


// With Initiailizing
class Welcome2{
    // __init__(self, name){
        // self.name = name
    // }
    //// Method
    hello(self) {
        return `Hello ${self.name}`
    }
}
//// Create A New Class
let user2 = new Welcome2("SALAH");
console.log(user2.name);
console.log(user2.hello());
