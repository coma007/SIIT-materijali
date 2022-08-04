// See https://aka.ms/new-console-template for more information

using System.Threading.Channels;

namespace Calculator

{
    class Calculator
    {
        
        
    }

    class Program
    {
        public static int Main()
        {
            Console.WriteLine("Input: ");
            string cmd = Console.ReadLine();
            if (cmd.Equals("exit") || cmd.Equals("kraj"))
            {
                Console.WriteLine("Exit");
                return 0;
            }

            List<string> args = ParseArgs(cmd);
            if (args.Count != 3)
            {
                Console.WriteLine("Error: number of args is not 3");
                return 0;
            }
            
            double result = DoMath(args);


            return 0;
        }

        public static double DoMath(List<string> args)
        {
            double val1, val2;
            
        }

        public static List<string> ParseArgs(string cmd)
        {
            List<string> args = new List<string>();
            string tmp = "";
            foreach (char c in cmd)
            {
                if (c == ' ')
                {
                    if (tmp != "")
                    {
                        args.Add(tmp);
                        tmp = "";
                    }
                }
                else
                {
                    tmp += c;
                }
            }
            if (tmp != "")
            {
                args.Add(tmp);
                tmp = "";
            }

            return args;
        }

    }
}