// Da li ce cinjenica da je account varijabla konstantna uticati na menjanje polja u njoj?
// Napraviti da je nemoguce promeniti polje account objekta.

const account = {
  username: "marijn",
  password: "xyzzy"
}

account.password = "s3cret"

console.log(account.password)
