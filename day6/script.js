function CountToN(x)
{
    let absx=Math.abs(x);

    let index=1;
    while(index<=absx)
    {
        console.log(index);
        index=index+1; //index++; index+=1
    }
}
CountToN (10);

const GetNumber = () =>
    {
        let num=Number(prompt("Enter a number"));
        if (isNaN(num))
        {
            return num;
        }
    }

const getNumber = () => {
    let num=GetNumber ();
    console.log(num + 10);
}
GetNumber()

//Task 4

function Multiples(x,m,Mult)
{
    let absx=Math.abs(x);

    let index=1;
    while(index<=absx)
    {
        Mult.push(m*index);
        index=index+1; //index++; index+=1
    }
}
let t=[]
Multiples(10,5,t)

