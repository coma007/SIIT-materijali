using System;

namespace StringSerialize
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string str = Console.ReadLine();
            using(StreamWriter writetext = new StreamWriter("text.txt"))
            {
                writetext.WriteLine(str);
            }

        }
    }
}