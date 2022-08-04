using System;
using System.Collections.Generic;

namespace Classes.SRP.Books
{
    /// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Refaktoriši kod tako da redukuješ broj odgovornosti koje Book klasa ispunjava.
    /// 2. Primeni "extract class", "extract method" ili "move method" refaktorisanja tokom ovog procesa.
    /// 3. Isprati da li novi dizajn može da podrži sledeće zahteve i dodatno dopuni i refaktoriši kod ako to nije slučaj:
    ///     a. Praćenje da li je isti čitalac pročitao knjigu više puta.
    ///     b. Praćenje kada je čitalac krenuo da čita knjigu i kada je završio.
    /// </summary>
    public class Book
    {
		public int Id { get; }
        public string Title { get; }
        public string Author { get; }
        public string Abstract { get; }
        public Dictionary<int, string> Pages { get; }
        public Dictionary<int, int> LastPageReadByReader { get; }

        public string StartReading(int readerId)
        {
            bool newReader = LastPageReadByReader.TryAdd(readerId, 0);
            return newReader ? Pages[0] : ContinueReading(readerId);
        }

        public string ContinueReading(int readerId)
        {
            int lastPageNumber = LastPageReadByReader[readerId];
            return Pages[lastPageNumber];
        }

        public string TurnPage(int newPage, int readerId)
        {
            if(!Pages.ContainsKey(newPage)) throw new InvalidOperationException("Book does not contain the requested page.");
            LastPageReadByReader[readerId] = newPage;
            return Pages[newPage];
        }
    }
}
