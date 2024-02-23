//  2.0.10 The var keyword - continued

//After this short introduction to functions (this is obviously not our last meeting with them) let's return to the
// keyword var and variable scopes.
//
// If we declare a variable using the keyword var inside a function, its scope will be limited only to the inside of
// that function (it's a local scope). This means that the variable name will be correctly recognized only inside
// this function.
//
// Let's consider the following example:

var  globalGreeting  =  "Good  ";

function  testFunction()  {
    var  localGreeting  =  "Morning  ";
    console.log("function:");
    console.log(globalGreeting);
    console.log(localGreeting);
}

testFunction();

console.log("main  program:");
console.log(globalGreeting);
console.log(localGreeting);  //  ->  Uncaught  ReferenceError:  localGreeting  is  not  defined

//First of all, run this program and observe the results on the console. What happened, and above all, why did it happen?
//
// Let's take a closer look at the code. In the example, we declared the global variable globalGreeting.
// Then we defined the testFunction function, inside which we declared the local variable localGreeting.
// Then we called the testFunction function, which resulted in writing out the values of both variables
// (inside the function, we have access to both the global variable and the local ones). Attempting to access
// the local variable localGreeting outside the function will fail. So we’ve finally succeeded in demonstrating
// that variable declarations using the word var can also be local.

