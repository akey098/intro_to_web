// #1
function parseJSON(jsonStr) {
    try {
        let parsedData = JSON.parse(jsonStr);
        console.log("Parsed Object:", parsedData);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

// #2
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;

for (let num of numbers) {
    console.log("Current number:", num);
    if (num % 2 === 0) {
        sum += num;
        console.log("Added to sum:", sum);
    }
}

console.log("Final sum of even numbers:", sum);

// Lab #3
let users = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 22 }
];

console.table(users);

// #4
function divide(a, b) {
    try {
        if (b === 0) {
            throw new Error();
        }
        return a / b;
    } catch (error) {
        console.error("Cannot divide by zero");
    }
}

console.log("Division result:", divide(10, 2));
console.log("Division result:", divide(10, 0));

// \#5
try {
    console.log(undefinedVariable);
} catch (error) {
    console.error("Variable is not defined");
}
