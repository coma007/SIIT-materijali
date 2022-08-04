using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Naming.Meaningful
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Razmotri opis sledeće metode i analiziraj njeno telo.
    /// 2. Sa boljim razumevanjem šta segmenti funkcije rade, preimenuj nazive identifikatora koji se koriste u telu WordExtractor klase.
    /// </summary>
    public class WordExtractor
    {
        /// <summary>
        /// The following function accepts a string that represents an identifier name and returns a list of words (individual + syntagms).
        /// </summary>
        /// <param name="nameString">The identifier name, expected in pascal case. E.g., "TowerOfBabel".</param>
        /// <returns>The list of words and syntagms. E.g., ["Tower", "Of", "Babel", "TowerOf", "TowerOfBabel", "OfBabel"]</returns>
        public static List<string> Extract(string nameString)
        {
            var wordList = Regex.Split(nameString, "[A-Z]");
            var letters = Regex.Matches(nameString, "[A-Z]");
            
            List<string> single = new();
            for (int i = 0; i < letters.Count; i++)
            {
                single.Add(letters[i] + wordList[i + 1]);
            }

            if (single.Count > 1)
            {
                List<string> multi = new List<string>();
                int s = 0;
                for (var i = 0; i <= single.Count - 2; i++)
                {
                    int e = single[i].Length;
                    for (var j = i + 1; j <= single.Count - 1; j++)
                    {
                        e += single[j].Length;
                        multi.Add(nameString.Substring(s, e));
                    }

                    s += single[i].Length;
                }

                single.AddRange(multi);
            }

            return single;
        }
    }
}
