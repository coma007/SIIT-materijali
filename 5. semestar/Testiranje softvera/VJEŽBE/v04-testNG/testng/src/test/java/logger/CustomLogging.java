package logger;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

public class CustomLogging implements ITestListener{

    //Called when the test-method execution starts
    @Override
    public void onTestStart(ITestResult result) {
        System.out.println("Test method started: "+ result.getName()+
                " and time is: "+getCurrentTime());
    }
    //Called when the test-method execution is a success
    @Override
    public void onTestSuccess(ITestResult result) {
        System.out.println("Test method success: "+ result.getName()+
                " and time is: "+getCurrentTime());

    }

    //Called when the test-method execution fails
    @Override
    public void onTestFailure(ITestResult result) {
        System.out.println("Test method failed: "+ result.getName()+
                "and time is: "+getCurrentTime());

    }
    //Called when the test-method is skipped
    @Override
    public void onTestSkipped(ITestResult result) {
        System.out.println("Test method skipped: "+ result.getName()+
                " and time is: "+getCurrentTime());
    }
    //Called when the test-method fails within success percentage
    @Override
    public void onTestFailedButWithinSuccessPercentage(ITestResult
                                                               result) {
        // Leaving blank

    }
    //Called when the test in xml suite starts
    @Override
    public void onStart(ITestContext context) {
        System.out.println("Test in a suite started: "+ context.
                getName()+ " and time is: "+getCurrentTime());

    }

    //Called when the test in xml suite finishes
    @Override
    public void onFinish(ITestContext context) {
        System.out.println("Test in a suite finished: "+ context.
                getName()+ " and time is: "+getCurrentTime());

    }

    //Returns the current time when the method is called
    public String getCurrentTime(){
        DateFormat dateFormat =
                new SimpleDateFormat("HH:mm:ss:SSS");
        Date dt = new Date();
        return dateFormat.format(dt);
    }
}
