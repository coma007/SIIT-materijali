package rs.ac.uns.testing.smartHouse;

import java.util.Calendar;

public class SmartHouseControllerRefactored {

    private Calendar lastMotionTime;
    private SmartHouseSystemRefactored smartHouseSystem;

    private IDateTimeProvider dateTimeProvider;

    public SmartHouseControllerRefactored(Calendar lastMotionTime, SmartHouseSystemRefactored smartHouseSystem, IDateTimeProvider dateTimeProvider) {
        this.lastMotionTime = lastMotionTime;
        this.smartHouseSystem = smartHouseSystem;
        this.dateTimeProvider = dateTimeProvider;
    }

    public String actuateLights(boolean motionDetected) {
        Calendar time = this.dateTimeProvider.getTime();

        // Update the time of last motion.
        if (motionDetected)
        {
            lastMotionTime = time;
        }

        // If motion was detected in the evening or at night, turn the light on.
        String timeOfDay = smartHouseSystem.getTimeOfDay(time);
        if (motionDetected && (timeOfDay.equals("Evening") || timeOfDay.equals("Night")))
        {
            return "ON";
        }
        // If no motion is detected for one minute, or if it is morning or day, turn the light off.
        else if ((time.getTimeInMillis() - lastMotionTime.getTimeInMillis()) > 60000 ||
                (timeOfDay.equals("Morning") || timeOfDay.equals("Noon")))
        {
            return "OFF";
        }

        return "OFF";
    }
}
