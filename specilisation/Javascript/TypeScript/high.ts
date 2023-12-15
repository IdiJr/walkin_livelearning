// Interfaces
interface Person {
    name: string
    age: number
    greet: () => void;
}

// The above interface defines the properties of an object

let user: Person = {
    name: "Bob",
    age: 21,
    greet: function() {
        console.log(`Hello, I'm ${this.name}.`);
    }
};
user.greet();

// Enums
enum color {
    Red,
    Green,
    Pink,
}
let mycolor: color = color.Pink;
console.log(mycolor)
