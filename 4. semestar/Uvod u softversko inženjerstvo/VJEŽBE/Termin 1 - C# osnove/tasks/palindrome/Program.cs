using System;

namespace Palindrome
{
    public class Program
    {
        public static void Main(string[] args)
        {
            System.Console.WriteLine(Palindrome("cicamaca"));
        }

        public static bool Palindrome(string str) {
            for (int i = 0; i <= str.Length/2; i++) {
                if (!str[i].Equals(str[str.Length-1-i])) {
                    return false;
                }
            }
            return true;
        }
    }
}