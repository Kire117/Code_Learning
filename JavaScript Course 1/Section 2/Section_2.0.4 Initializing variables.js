// After a successful declaration, the variable should be initialized, in other words, it should be given its first
// value. Initialization is done by assigning a certain value to a variable (indicated by its name). To assign it,
// we use the operator =.

//You can assign to a variable: a specific value; the contents of another variable; or, for example, the result
// returned by a function.

//Initialization can be done either together with the declaration, or separately as an independent command.
// It is important to enter the first value into the variable before trying to read, modify, or display it.


let height = 180;
let anotherHeight = height;
let weight;
console.log(height); // -> 180
console.log(anotherHeight); // -> 180
weight = 70;
console.log(weight); // -> 70

// By the way, pay attention to one thing. If you specify a variable name in console.log, the interpreter recognizes it and displays its value. If you put the same name in quotation marks, it will be treated as plain text, and displayed as such.
//
console.log("height"); // -> height
// let height = 180;
// console.log(height); // -> 180





