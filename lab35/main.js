//#1
for (let i =0; i <= 10; i++){
  console.log(i)
}

//#2
n =10
while(n > 0){
  console.log(n);
  n--;
}

//#3
let userInput;
do{
  userInput = parseInt(prompt("Enter num greater than 10:"), 10)
} while (userInput <= 10);
console.log("Valid input recieved: ", userInput);

//#4
let fruits = ['Banana', 'Apple', 'Mango', 'Pineapple', 'Orange'];
for(let i = 0; i < fruits.length; i++){
  console.log(fruits[i])
}

//#5

let fruits = ['Banana', 'Apple', 'Mango', 'Pineapple', 'Orange'];

let i = 0;
while(i<fruits.length){
  console.log(fruits[i]);
  i++;
}

//#6
let nums = [3, 7, 12, 5, 9]
for(let i =0; i< nums.length; i++){
  if (nums[i] === 12){
    console.log("Success!")
    break
  }
  console.log(nums[i])
}

//#7
let nums = [3, 7, 12, 5, 9]
for(let i =0; i< nums.length; i++){
  if (nums[i] === 5){

    continue
  }
  console.log(nums[i])
}