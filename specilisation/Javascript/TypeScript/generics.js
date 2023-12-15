// Generic typescript
function indentity(arg) {
    return arg;
}
// Usage
var result = indentity(56);
console.log(result);
var message = indentity("Hello, Kofi!");
console.log(message);
// Generics can be restricted (generic function with constraint)
function printName(obj) {
    console.log(obj.name);
}
// Usage
var person = { name: "John", age: 27 };
printName(person);
var animal = { name: "Lion", sound: "Roar" };
printName(animal);
