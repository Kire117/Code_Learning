//Until now, we assumed that after declaring a variable, its name could be used in the whole code of the program
// (i.e. the scope of the variable is global). This is not entirely true – the scope of a variable depends on where
// it is declared. Unfortunately, for a good understanding of variable scope, we need to learn a few more programming
// elements, such as conditional instructions or functions, which will be discussed in more detail later in the course.
// So here we will limit ourselves to basic information, and will come back to this issue in different parts of the
// course. One of the basic elements that influence the scope of variables is a program block.

//Program blocks
// We can separate the code of a program into blocks. In the blocks that we create using curly brackets,
// there is a set of instructions, which for some reason should be treated independently. The blocks are usually
// associated with conditional instructions, loops, or functions, which we will talk about later. We can also separate
// a block of a program unrelated to anything special, simply by choosing a certain range of instructions
// (in practice, this is not particularly justified, and for now we will only do it for educational reasons).
//
// Let's look at an example:

let  counter;
console.log(counter);  //  ->  undefined
{
    counter  =  1;
    console.log(counter);  //  ->  1
}
counter  =  counter  +  1;
console.log(counter);  //  ->  2

//First, we declare the variable counter. Then we open a block inside which we initialize this variable and display its
// contents. Outside the block, we increase the value stored in the variable by 1 and display it again. In this case,
// the interpreter will execute the program as if it hadn't noticed the block, going through the instructions before
// the block, in the block, and after the block. Creating a block here, without, for example, conditional instructions,
// has no real justification – it is just an example of using brackets.

//Program blocks can be nested, that is, we can create one block inside of another one.
let  counter;
console.log(counter);  //  ->  undefined
{
    counter  =  1;
    {
        console.log(counter);  //  ->  1
    }
}
counter  =  counter  +  1;
console.log(counter);  //  ->  2

//By the way, please note that the code inside the block has been moved to the right. This is called an indentation.
// For a JavaScript interpreter, it doesn't matter at all, but it definitely increases the readability of the code,
// allowing the readers (including you) to quickly find out which parts of the code are inside, and which are outside,
// the block. Code editors usually add indentations in the right places by themselves, but it is a good habit to
// remember this yourself and, if they do not appear automatically, format the code by hand.

//let and const
// It's time to move on to determine what is actually going on with these scopes. Unfortunately, the scopes of variables
// (and constants) declared with let and const look slightly different than those declared with var. So we will discuss
// them independently.
//
// The first rule is simple. If we declare any variable or constant using let or const, respectively, outside the code
// blocks, they will be global. By this we mean that their names will be visible throughout the program, outside blocks,
// inside blocks, in functions, and so on. We will be able to refer to them anywhere by their names, and of course have
// access to their values.
//
// What happens if we declare something using let or const inside a block? This will create a local variable or
// constant. It will be visible only inside the block in which it was declared and in blocks that can optionally be
// nested in it.
//
// Let's look at a simple example:
let  height  =  180;
{
    let  weight  =  70;
    console.log(height);  //  ->  180
    console.log(weight);  //  ->  70
}
console.log(height);  //  ->  180
console.log(weight);  //  ->  Uncaught  ReferenceError:  weight  is  not  defined

//The height variable, declared outside the block, is global. The weight variable is local – its scope is limited by
// the block in which it was declared. This is clearly visible when trying to display the values of both variables
// inside and outside the block. We can also test the case with nested blocks:

let  height  =  200;
{
    let  weight  =  100;
    {
        let  info  =  "tall";
        console.log(height);  //  ->  200
        console.log(weight);  //  ->  100
        console.log(info);  //  ->  tall
    }
    console.log(height);  //  ->  200
    console.log(weight);  //  ->  100
    console.log(info);  //  ->  Uncaught  ReferenceError:  info  is  not  defined
}
//As you can see, the info variable declared in the most internal block is visible only inside it.
// The weight variable is visible both inside the block in which it was declared and inside the block nested in it.
// And the global variable height is visible everywhere.
//
// Simple, isn't it?

//      var

//In the case of variable declarations using the keyword var, the situation is slightly different.
// The variable declared using it outside the blocks will, as in the case of let, be global, in other words,
// it will be visible everywhere. If you declare it inside a block, then... well, it will usually turn out to be
// global again.
//
// Let's start with a simple example:

var  height  =  180;
{
    var  weight  =  70;
    console.log(height);  //  ->  180
    console.log(weight);  //  ->  70
}
console.log(height);  //  ->  180
console.log(weight);  //  ->  70

//As expected, both variables, height and weight, turn out to be global. Will the variables declared using var always,
// regardless of the place of declaration, be global? Definitely not. The problem is that var ignores ordinary program
// blocks, treating them as if they do not exist. So in what situation can we declare a local variable using var?
// Only inside a function. We will devote a lot of space to discussing the function, and then we will come back to
// the problem of the variable scope as well. Now we will try to present and discuss only a simple example, which will
// show that var variables are sometimes local, too.