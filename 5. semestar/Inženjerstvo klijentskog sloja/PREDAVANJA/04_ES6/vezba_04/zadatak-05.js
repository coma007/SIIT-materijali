  /*
   * Napisati funkcija koja ima 3 parametra:
   * greeting, firstName, i lastName
   *
   * Postaviti podrazumevane vrednosti za firstName i lastName na "hello".
   */
   
   const greeting = () => {
     console.log(this);
   }
   console.log(greeting());
   console.log(greeting('hi', 'harry', 'hedger'));
