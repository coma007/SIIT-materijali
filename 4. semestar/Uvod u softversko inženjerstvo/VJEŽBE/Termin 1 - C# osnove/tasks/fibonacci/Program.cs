using System;

namespace Fibonacci {

    class Program {

        public static void Main(string[] args) {    
            System.Console.WriteLine(Fibonacci(8));
        }

        public static int Fibonacci(int num) {
            if (num <= 2) {
                return 1;
            }
            else {
                return Fibonacci(num-1) + Fibonacci(num-2);
            }
        }
    }
}