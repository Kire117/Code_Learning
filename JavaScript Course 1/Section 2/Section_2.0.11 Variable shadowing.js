//  2.0.11 Variable shadowing

//JavaScript allows for variable shadowing. What does that mean? It means that we can declare a global variable and a
// local variable of the same name.
//
// In the local scope, in which we declare a local variable using its name, we will have access to the local value
// (the global variable is hidden behind the local one, so we do not have access to it in this local scope).
// Using this name outside the local scope means that we will be referring to the global variable.
// This is not best programming practice, however, and we should avoid such situations.
// It is not difficult to guess that with a bit of inattention, using this mechanism can lead to unintended situations
// and probably to errors in the operation of the program.
//
// If we are to avoid such situations, it would be good to see exactly what they are about.
// Let's begin with an example without shadowing:

let  counter  =  100;
console.log(counter);  //  ->  100
{
    counter  =  200;
    console.log(counter);  //  ->  200
}
console.log(counter);  //  ->  200

//The counter variable, declared at the beginning of the program, is a global variable.
// Throughout the program, also inside the block, we operate on this very variable.
// A small change in the code is enough for the program to behave completely differently.

let  counter  =  100;
console.log(counter);  //  ->  100
{
    let  counter  =  200;
    console.log(counter);  //  ->  200
}
console.log(counter);  //  ->  100

//You see the difference? This time in the block, instead of counter = 200; (i.e. changes in the contents of the
// global counter variable), the let counter = 200; statement appears (i.e. declarations of the local variable
// combined with its initialization). The interpreter would consider such a situation to be wrong if the
// re-declaration appeared in the same scope.
//
// However, the declaration is local (it’s a different scope than global) and all references to the variable with
// this name inside the block will refer to this local variable. Outside the block, the global variable will still
// be seen under the same name. Pay attention to the values displayed by the console.




