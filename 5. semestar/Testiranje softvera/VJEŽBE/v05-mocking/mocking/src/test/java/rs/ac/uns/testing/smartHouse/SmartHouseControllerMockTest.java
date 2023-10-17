package rs.ac.uns.testing.smartHouse;

import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import rs.ac.uns.testing.user.User;

import java.util.Calendar;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.testng.AssertJUnit.assertEquals;

// In order to have clean unit test of controller class we need to mock all objects that can create errors
public class SmartHouseControllerMockTest {

    private static final Long morningTime = 1665374400000l;

    private Calendar lastMotionTime;

    // object under test
    private SmartHouseControllerRefactored smartHouseController;

    // object to be mocked
    private SmartHouseSystemRefactored smartHouseSystem;

    // object to be mocked
    private IDateTimeProvider dateTimeProvider;

    @BeforeMethod
    public void setup() {
        smartHouseSystem = createSmartHouseSystem();
        dateTimeProvider = createDateTimeProvider();

        lastMotionTime = Calendar.getInstance();

        smartHouseController = new SmartHouseControllerRefactored(Calendar.getInstance(), smartHouseSystem, dateTimeProvider);
    }

    @Test
    public void actuateLights_motionDetectedInEvening_ReturnsOn() {
        when(smartHouseSystem.getTimeOfDay(null)).thenReturn("Evening");

        String actual = this.smartHouseController.actuateLights(true);
        assertEquals( "ON", actual);
    }

    @Test
    public void actuateLights_motionDetectedInNight_ReturnsOn() {
        when(smartHouseSystem.getTimeOfDay(null)).thenReturn("Night");

        String actual = this.smartHouseController.actuateLights(true);
        assertEquals( "ON", actual);
    }

    @Test
    public void actuateLights_motionDetectedInMorning_ReturnsOff() {
        // stubb current time to Mon Oct 10 2022 06:00:00
        when(dateTimeProvider.getTime()).thenAnswer(
                invocation -> {
                    Calendar c = Calendar.getInstance();
                    c.setTimeInMillis(morningTime);
                    return c;
                });

        when(smartHouseSystem.getTimeOfDay(any(Calendar.class))).thenReturn("Morning");

        lastMotionTime = dateTimeProvider.getTime();

        String actual = this.smartHouseController.actuateLights(true);
        assertEquals( "OFF", actual);
    }

    @Test
    public void actuateLights_motionDetectedInNight_ReturnsOff() {
        // stubb current time now + 30 seconds
        when(dateTimeProvider.getTime()).thenAnswer(
                invocation -> {
                    Calendar c = Calendar.getInstance();
                    c.setTimeInMillis(lastMotionTime.getTimeInMillis() + 70000);
                    return c;
                });

        when(smartHouseSystem.getTimeOfDay(any(Calendar.class))).thenReturn("Night");

        String actual = this.smartHouseController.actuateLights(false);
        assertEquals( "OFF", actual);
    }

    private SmartHouseSystemRefactored createSmartHouseSystem() {
        SmartHouseSystemRefactored mock = mock(SmartHouseSystemRefactored.class);
        return mock;
    }

    private IDateTimeProvider createDateTimeProvider() {
        IDateTimeProvider mock = mock(IDateTimeProvider.class);
        return mock;
    }
}
