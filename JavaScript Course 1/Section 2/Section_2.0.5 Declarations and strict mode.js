// JavaScript had some major changes introduced in 2009 and 2015. Most of these changes extended the language syntax
// with new elements, but some of them concerned only the operation of the JavaScript interpreters. Often it was about
// clarifying the interpreters' behavior in potentially erroneous situations, such as in cases of variable
// initialization without any prior declaration.
//
// Let's look at an example:
height = 180;
console.log(height); // -> 180

//At first glance, you can see that we’ve forgotten to declare the variable height. The original JavaScript syntax
// allowed for such negligence, and at the moment of initialization it made this declaration for us. It seems like
// quite a good solution, but unfortunately it can sometimes lead to ambiguous and potentially erroneous situations
// (we’ll say a few more words about it while discussing the scope).
//
// Let's modify our example:
"use strict";
//
// height = 180; // -> Uncaught ReferenceError: height is not defined
// console.log(height);

//At the beginning of our code, we’ve added "use strict";. This statement has radically changed the behavior of the
// interpreter. Why? We use it when we want to force the interpreter to behave according to modern JavaScript standards.
// So, as long as you aren’t running some really old code, you should always use it. And this time, using a variable
// without its previous declaration is treated as an error.
// The sentence "use strict"; must be placed at the very beginning of the code. It will cause the interpreter to deal
// with the rest of the code using strict mode, which is the modern JavaScript standard. All further examples in our
// course will be prepared to work in this mode by default, even if "use strict"; does not always appear at the
// beginning of the code.



