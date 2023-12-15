function greet(name: string):string {
    return `Hello, ${name}!`;
}

const message: string = greet("TypeScript");
console.log(message);

// in the above function, name is defined as a string
// and only strings can be passed as names, else
// compilation will fail

let age: number = 25;
let isStudent: boolean = true;

// Array
let numbers: number[] = [1, 3, 5];
let names: string[] = ["John", "J'oans"];

function add(x: number, y: number): void{
    console.log(x+y);
}

console.log("\n");
console.log(numbers, names);
add(3, 7);

// objects
let person: {name: string; age: number} = {
    name: "Alice",
    age: 18,
}
console.log(person);

// in the person function, name only takes string inputs
// and age takes only numbers as input