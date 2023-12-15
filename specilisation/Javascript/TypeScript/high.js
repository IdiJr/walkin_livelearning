// The above interface defines the properties of an object
var user = {
    name: "Bob",
    age: 21,
    greet: function () {
        console.log("Hello, I'm " + this.name + ".");
    }
};
user.greet();
