class BankAccount {
    constructor(id, fname, lname, saldo) {
        this.fname = fname;
        this.lname = lname;
        this.saldo = saldo;
        this.transactions = [];
    }
    
    add(money) {
        this.saldo += money;
        this.transactions.push(money);
        console.log("Succesfull payment");
    }
    
    remove(money) {
        this.saldo -= money;
        this.transactions.push(-money);
        
        console.log("Succesfull payoff");
    }
}

u1 = new BankAccount(1, "Fika", "Fikic", 200);
u1.add(200);
u1.add(200);
u1.add(200);
u1.remove(140);
u1.remove(20);
u1.add(20);
console.log(u1.transactions)

