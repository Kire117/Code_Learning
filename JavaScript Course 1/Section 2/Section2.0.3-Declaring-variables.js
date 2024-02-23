var  height;
console.log(height);  //  ->  undefined
console.log(weight);  //  ->  Uncaught  ReferenceError:  weight  is  not  defined


/*The first line is the variable declaration (we can see the var keyword). This declaration means that the word
height will be treated as the name of the container for certain values.*/

/*The declaration, like other JavaScript instructions, should end with a semicolon. In the second line, we try to write
 out the value of this variable (that is, what is in the container) on the console. Because we haven't put anything
 there yet, the result is undefined (the interpreter knows this variable, but it has no value yet – the value is
 undefined). In the next line, we try to print out the contents of the weight variable ... which we forgot to declare.
 This time, we will see ReferenceError. The JavaScript interpreter, which executes our program, has informed us that it
does not know a variable by this name (so the variable itself is undefined).*/

//The alternative to it is the keyword let. We use both keywords in the same way. Both are meant for declaring variables
// , and both can be found in different examples on the Internet or in books. However, they are not exactly the same,
// and we’ll discuss the differences in their operation later in this chapter (even in several places).
//
// The keyword var comes from the original JavaScript syntax, and the keyword let was introduced much later. Therefore,
// you will find var more in older programs. Currently, it is highly recommended to use the word let for reasons that
// we’ll discuss in a moment.
//
// So, let's take a look at our example rewritten this time using the keyword let.
//
//
let height;
console.log(height); // -> undefined

//One of the basic differences in the use of var and let is that let prevents us from declaring another variable with
// the same name (an error is generated). Using var allows you to re-declare a variable, which can potentially lead to
// errors in the program execution.
//
//
var height;
var height;
 console.log(height); // -> undefined

//The example above demonstrates the possibility of re-declaring a variable using the keyword var. In this situation,
// it will not cause an error, but in more complex programs a redeclaration, especially by accident, may no longer be
// without consequences. When declaring with let, the interpreter checks whether such a variable has already been
// declared, no matter if let or var is used in the previous declaration.
//
//
 let height;
 let height; // -> Uncaught SyntaxError: Identifier 'height' has already been declared
console.log(height);

//So use let to declare variables, if only because you don't want to accidentally declare a variable again.
