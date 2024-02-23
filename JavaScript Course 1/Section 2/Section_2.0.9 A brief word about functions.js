//2.0.9 A brief word about functions


//Let's start by explaining what functions are. It often happens that a certain piece of code, performing some specific
// task, will be used many times. Yes, you can copy this piece of code, all of its instructions, to any place where you
// want to use it. However, this would be very inefficient. First of all, the size of our program would grow
// unnecessarily. Secondly, if we would like to make some changes to this piece of code, for example, to correct some
// bug, we would have to do it in every place where we used it.
//
// A simple solution to this problem is a function. A function is just a separated piece of code that you name, in the
// same way that you name a variable. If you want to use it somewhere, you simply refer to it using that name
// (we say that we call the function).
//
// The declaration of a simple function, let's say testFunction, may look like this:
function  testFunction()  {
    console.log("Hello");
    console.log("World");
}

//The way to define the function shown in the example is one of several available in JavaScript. The definition starts
// with the function keyword, followed by the function name we invented. After the name, you see parentheses, which
// optionally could contain parameters passed to the function (we will come back to this when we discuss the function
// more precisely). Then we open the program block, which contains the instructions belonging to the function.
// When defining a function, the instructions contained in the function are not executed. To execute the function,
// you must call it independently, using its name.

console.log("let's  begin:");  //  ->  let's  begin:
console.log("Hello");  //  ->  Hello
console.log("World");  //  ->  World
console.log("and  again:");  //  ->  and  again:
console.log("Hello");  //  ->  Hello
console.log("World");  //  ->  World
console.log("and  once  more:");  //  ->  and  once  more:
console.log("Hello");  //  ->  Hello
console.log("World");  //  ->  World














