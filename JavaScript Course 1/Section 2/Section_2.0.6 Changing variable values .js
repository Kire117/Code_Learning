//Variables, as their name suggests, can store data that will vary. Changes are made by assigning a new value to
// the variable, which overwrites the previous one.

let  steps  =  100;
console.log(steps);  //  ->  100
steps  =  120;  //  ->  120
console.log(steps);
steps  =  steps  +  200;
console.log(steps);  //  ->  320

//Variables in the JavaScript language are untyped (or, to be more precise, they are weakly and dynamically typed).
// This means that JavaScript will not control what type of value we store in the variable. What exactly is the data
// type? You can probably intuitively answer this question yourself. The type determines the belonging of a given data
// to a certain set that share the same properties and on which you can perform the same operations. Data types vary
// greatly depending on the programming language. In JavaScript, the main types are number and character string.
// We will talk much more about types in the next chapter. Let's declare a few variables and initialize them with
// values of different types:

let  greeting  =  "Hello!";
let  counter  =  100;

//As you can see, the greeting variable is initiated with a value of the string type, while the counter variable is
// initiated with a value of the number type. Continuing the example, we will make a small change in the contents of
// the greeting variable.

console.log(greeting);  //  ->  Hello!
greeting  =  1;
console.log(greeting);  //  ->  1

//JavaScript allows us to easily replace the greeting variable with a value whose type is different from the one
// originally stored there. JavaScript goes one step further and not only allows us to change the types of values
// kept in a variable, but it also performs their implicit conversion if necessary (we will also return to this topic
// of conversion when discussing types). Let's restore the original value of the greeting variable and then add the
// value of the counter variable to it.

greeting  =  "Hello!";
greeting  =  greeting  +  counter;
console.log(greeting);  //  ->  Hello!100

//The interpreter will check the type of value stored in the greeting variable and convert the value from the counter
// variable to the same type before performing an addition operation. As a result, the string "100" will be added to
// the "Hello!" character string and stored to the greeting variable. By the way, note that JavaScript interprets 100
//  as a number, but "100" as a string.
