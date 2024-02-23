//The JavaScript interpreter scans the program before running it, looking for errors in its syntax, among other things.
// It does one more thing on this occasion. It searches for all variable declarations and moves them to the beginning
// of the range in which they were declared (to the beginning of the program if they are global, to the beginning of
// the block if it is a local let declaration, or to the beginning of the function if it is a local var declaration).
// All this happens, of course, in the interpreter memory, and the changes are not visible in the code.
//
// Hoisting, because we are talking about it, is a rather complex and frankly speaking quite incoherent mechanism.
// Understanding it well requires the ability to freely use many JavaScript elements, which we have not even mentioned yet.
//
// What's more, it's rather a curiosity than something practical that you will use when writing programs, so we will
// look at just one small example that will allow us to roughly understand the very principle of hoisting.
// This may make it easier for you to understand some surprising situations when writing your own code, or testing
// examples you find in various sources.

var  height  =  180;
console.log(height);    //  ->  180
console.log(weight);    //  ->  Uncaught  ReferenceError:  weight  is  not  defined

//In the above example, we forgot to declare the variable weight. The result is obvious:
// we’re referring to a variable (that is, we’re trying to read its contents) which does not exist.
// Something like this must end in an error.
//
// Let's make a small change:
var  height  =  180;
console.log(height);    //  ->  180
console.log(weight);    //  ->  undefined
var  weight  =  70;
console.log(weight);    //  ->  70

//This time we declared our variable, but in a rather strange place. Together with the declaration, we also performed
// initialization. The result of the program may be a bit surprising. This time there are no errors. Hoisting has worked,
// and the declaration has been moved by the interpreter to the beginning of the range (in this case the program).
//
// However, the attempt to display the contents of the weight variable give two different results. Why? Hoisting
// only concerns the declaration, not initialization. So the value 70, which we assign to the weight variable, remains
// on the line where the original declaration is. The above example is interpreted by the JavaScript engine more or
// less in the following way:

//Hoisting unfortunately works a little differently with the let and const declarations.
//
// However, we will not go into it. It is enough that you are aware of the phenomenon.
//
// And most of all, you will remember ALWAYS to declare variables before using them.
