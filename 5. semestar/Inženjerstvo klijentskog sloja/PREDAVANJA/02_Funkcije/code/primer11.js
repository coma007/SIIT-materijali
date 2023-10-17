var calculator = {
  value: 0,
  add: function (x) {
    this.value += x;
    return this;
  },
  subtract: function (x) {
    this.value -= x;
    return this;
  }
};

calculator.add(5).add(7).subtract(10);
console.log(calculator.value);
