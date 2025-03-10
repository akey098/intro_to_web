// #1
function sum(a,b) {
    return a+b;
}
console.log(sum(4, 5));

function square(a){
    return a*a;
}
console.log(square(6));

function max (a,b) {
    return a>b ? a:b;
}
console.log(max(7, 3));

// #2
let message = "Hello from global";
function printMessage() {
    let message = "Hello from local";
    console.log("Inside function:", message); // Logs the local variable value
}
printMessage();

function helloGlobal() {
    let localMessage = "Hello from function scope";
    console.log(localMessage);
}
helloGlobal();
console.log(localMessage);


// #3
if (true) {
    var varVar = "This is var";
}
console.log(varVar);
if (true) {
    let letVar = "This is let";
    const constVar = "This is const";
    console.log(letVar);
    console.log(constVar);
}
console.log(letVar);
console.log(constVar);

// #4
function counter() {
      let counter = 0;
      return function() {
          counter++;
          return counter;
      };
   }

   const count1 = counter();
   console.log(count1());
   console.log(count1());

   const count2 = counter();
   console.log(count2());
