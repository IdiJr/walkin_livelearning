// Generic typescript
function indentity<T>(arg: T): T {
    return arg;
}

// Usage
let result: number = indentity<number>(56);
console.log(result);

let message: string = indentity<string>("Hello, Kofi!")
console.log(message);

// Generics can be restricted (generic function with constraint)
function printName<T extends {name: string}>(obj: T): void {
    console.log(obj.name);
}

// Usage
let person = {name: "John", age: 27};
printName(person);

let animal = { name: "Lion", sound: "Roar"};
printName(animal);