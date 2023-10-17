package rs.ac.uns.testing.smartHouse;

import java.util.Calendar;

public class SmartHouseSystem {

    public String getTimeOfDay()
    {
        Calendar time = Calendar.getInstance();

        if (time.get(Calendar.HOUR_OF_DAY) >= 0 && time.get(Calendar.HOUR_OF_DAY) < 6)
        {
            return "Night";
        }
        if (time.get(Calendar.HOUR_OF_DAY) >= 6 && time.get(Calendar.HOUR_OF_DAY) < 12)
        {
            return "Morning";
        }
        if (time.get(Calendar.HOUR_OF_DAY) >= 12 && time.get(Calendar.HOUR_OF_DAY) < 18)
        {
            return "Afternoon";
        }
        return "Evening";
    }

}
