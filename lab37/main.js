// #1

let fruits = [];
fruits.push("apple", "banana", "cherry");
let removedFruit = fruits.pop();
console.log("Removed fruit:", removedFruit);
console.log("Final array:", fruits);

// #2

let numbers = [10, 20, 30, 40, 50];
let slicedNumbers = numbers.slice(1, 4);
console.log("Sliced array:", slicedNumbers);
console.log("Original array:", numbers);

// #3

let nums = [1, 2, 3, 4, 5];
let squaredNums = nums.map(num => num * num);
console.log("Original array:", nums);
console.log("Squared array:", squaredNums);

// #4

let ages = [12, 18, 25, 30, 15];
let filteredAges = ages.filter(age => age >= 18);
console.log("Filtered array:", filteredAges);

// #5

let user = {
    name: "Alice",
    age: 25,
    city: "New York"
};
console.log("Name:", user.name);
user.age = 26;
console.log("Updated user:", user);

// #6

let car = { brand: "Tesla", model: "Model S", year: 2023 };

console.log("Keys:", Object.keys(car));
console.log("Values:", Object.values(car));


