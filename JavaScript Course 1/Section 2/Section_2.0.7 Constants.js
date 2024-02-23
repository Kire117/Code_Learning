//The const keyword is used to declare containers similar to variables. Such containers are called constants.
// Constants are also used to store certain values, but once values have been entered into them during initialization,
// they can no longer be modified. This means that this type of container is simultaneously declared and initialized.
// For example, the following declaration of the greeting constant is correct:

const  greeting  =  "Hello!";

//But this next one definitely causes an error:
//const  greeting;  //  ->  Uncaught  SyntaxError:  Missing  initializer  in  const  declaration
//greeting  =  "Hello!";

//As we said, a change in the constant is impossible. This time the declaration is correct, but we try to modify the
// value stored in the constant.
// const greeting = "Hello!";
// greeting = "Hi!"; // -> Uncaught TypeError: Assignment to constant variable.

//The main purpose of a constant is to eradicate the possibility of accidentally changing a value stored in it.
// This is important when we have some values that really should never change. Typical examples of constants
// are paths to resources, tokens, and other data that never change throughout the lifetime of the script.
//
// But constants can also be used as sub results in calculations or in other places where whatever information
// was gathered or calculated will not change any further. Using a const, besides preventing a value from being
// changed by mistake, allows the JavaScript engine to optimize the code, which may affect its performance.



