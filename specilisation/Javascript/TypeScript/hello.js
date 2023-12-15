function greet(name) {
    return "Hello, " + name + "!";
}
var message = greet("TypeScript");
console.log(message);
// in the above function, name is defined as a string
// and only strings can be passed as names, else
// compilation will fail
var age = 25;
var isStudent = true;
// Array
var numbers = [1, 3, 5];
var names = ["John", "J'oans"];
function add(x, y) {
    console.log(x + y);
}
console.log("\n");
console.log(numbers, names);
add(3, 7);
// objects
var person = {
    name: "Alice",
    age: 18
};
console.log(person);
