package rs.ac.uns.testing.smartHouse;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.Calendar;

public class SmartHouseSystemTest {

    @Test
    public void getTimeOfDay_For6AM_ReturnsMorning() {
        SmartHouseSystemRefactored smartHouse = new SmartHouseSystemRefactored();

        Calendar time = Calendar.getInstance();
        time.set(Calendar.HOUR_OF_DAY, 6);

        String actual = smartHouse.getTimeOfDay(time);

        Assert.assertEquals(actual, "Morning");
    }

    @Test
    public void getTimeOfDay_For12AM_ReturnsAfternoon() {
        SmartHouseSystemRefactored smartHouse = new SmartHouseSystemRefactored();

        Calendar time = Calendar.getInstance();
        time.set(Calendar.HOUR_OF_DAY, 12);

        String actual = smartHouse.getTimeOfDay(time);

        Assert.assertEquals(actual, "Afternoon");
    }
}
