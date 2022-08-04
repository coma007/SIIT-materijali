using System;
using System.Collections.Generic;

namespace Classes.Coupling.Rental
{
	/// <summary>
    /// ID izazova je dostupan na web prikazu.
    /// 1. Refaktoriši kod tako da redukuješ snagu spregnutosti između RentalSchedule i DateRange klase.
    /// </summary>
    public class RentalSchedule
    {
        int carId;
        List<DateRange> bookings;

        bool IsCarAvailable(DateTime onDay)
        {
            foreach (var booking in bookings)
            {
                if (booking.From > booking.To) throw new InvalidOperationException();
                if (booking.From > onDay && booking.To < onDay) return false; //Car is rented during this period.
            }
            return true;
        }
    }

    public class DateRange
    {
        public DateTime From { get; }
        public DateTime To { get; }
    }
}
