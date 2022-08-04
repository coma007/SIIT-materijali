using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Methods.Nesting
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Razmotri sledeći kod i pojednostavi ga tako što ćeš izdvojiti složene celine u zasebne metode.
    /// </summary>
    public class WordExtractor
    {
        public static List<string> ExtractWordsAndSyntagms(string pascalCaseName)
        {
            List<string> singleWords = GetSingleWords(pascalCaseName);
             if (singleWords.Count <= 1) return singleWords;
            // Syntagms are sets of more than 1 connected word
            List<string> syntagms = GetSyntagms(singleWords, pascalCaseName);
            singleWords.AddRange(syntagms);

            return singleWords;
        }

        public static List<string> GetSingleWords(string pascalCaseName) {
            MatchCollection capitalLetters = Regex.Matches(pascalCaseName, "[A-Z]");

            string[] wordsSplitByCapitalLetters = Regex.Split(pascalCaseName, "[A-Z]");
            List<string> singleWords = new();
            for (int i = 0; i < capitalLetters.Count; i++)
            {
                AddToSingleWords(singleWords, capitalLetters, wordsSplitByCapitalLetters, i);
                }
            return singleWords;
        }

        public static List<string> GetSyntagms(List<string> singleWords, string pascalCaseName) {
            List<string> syntagms = new List<string>();
                int startLength = 0;
                for (var i = 0; i <= singleWords.Count - 2; i++)
                {
                    int endLength = singleWords[i].Length;
                    for (var j = i + 1; j <= singleWords.Count - 1; j++)
                    {
                        endLength += singleWords[j].Length;
                        AddSyntagms(syntagms, pascalCaseName, startLength, endLength);
                    }
                    startLength += singleWords[i].Length;
                }
            return syntagms;
        }


        public static void AddSyntagms(List<string> syntagms, string pascalCaseName, int startLength, int endLength)
        {
            syntagms.Add(pascalCaseName.Substring(startLength, endLength));
        }

        public static void AddToSingleWords(List<string> singleWords, MatchCollection capitalLetters, string[] wordsSplitByCapitalLetters, int i) {
                singleWords.Add(capitalLetters[i] + wordsSplitByCapitalLetters[i + 1]);
        }


    }
}
