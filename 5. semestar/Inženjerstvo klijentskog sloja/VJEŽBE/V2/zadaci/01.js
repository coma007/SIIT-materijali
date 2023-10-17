const reciepts = [40, 145, 260];

function countTax(price) {
    return price * 1.01;
}

for (const price of reciepts) {
    console.log(countTax(price));
}
