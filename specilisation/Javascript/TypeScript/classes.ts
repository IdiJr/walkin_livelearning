// Interface
interface pet {
    name: string
    age: number
    greet: () => void;
}

// The above interface defines the properties of an object

let pet: pet = {
    name: "Spike",
    age: 6,
    greet: function() {
        console.log(`Hello, I'm ${this.name}.`);
    }
};
pet.greet();

// Classes
class Animal {
    private type: string

    constructor(type: string) {
        this.type = type;
    }

    makeSound(): string {
        return "Generic animal sound";
    }
}

class Dog extends Animal {
    constructor() {
        super("Dog");
    }

    makeSound(): string {
        return "Woof!"
    }
}

const myDog: Dog = new Dog();
console.log(myDog.makeSound());
