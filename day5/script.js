console.log('1');
console.log('2');
console.log('3');
console.log('4');
console.log('5');
console.log('6');
console.log('7');
console.log('8');
console.log('9');
console.log('10');

// With One Line
console.log('1\n2\n3\n4\n5\n6\n7\n8\n9\n10')

// prompt
// let result= prompt("Enter Your Name")
// console.log("Hello", result);

//let num = prompt("Enter A Number");
//num= Number(num);

//if (isNaN(num)) 
{
    num=10
}

// num= num +10;
// console.log(num); 

//Task 3
let result= prompt("Enter your grade")
let grade= Number(result);
if (!isNaN(grade)){
    if (grade>=70) {
    console.log('You passed!')
    }else{
    console.log("You failed.")
    }
}else{
    console.log("is not a numerical value")
}

