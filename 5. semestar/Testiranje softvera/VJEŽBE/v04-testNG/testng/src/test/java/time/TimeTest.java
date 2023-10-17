package time;

import org.testng.annotations.Test;

public class TimeTest {

    @Test(timeOut=500)
    public void timeTestOne() throws InterruptedException{
        Thread.sleep(1000);
        System.out.println("Time test method one");
    }

    @Test
    public void timeTestTwo() throws InterruptedException{
        Thread.sleep(400);
        System.out.println("Time test method two");
    }
}
