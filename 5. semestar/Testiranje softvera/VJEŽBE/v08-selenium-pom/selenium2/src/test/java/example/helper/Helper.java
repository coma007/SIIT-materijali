package example.helper;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

import java.io.File;
import java.io.IOException;

public class Helper {

    public static void takeScreenshoot(WebDriver driver, String name) {
        TakesScreenshot ts = (TakesScreenshot) driver;

        //capture screenshot as output type FILE
        File file = ts.getScreenshotAs(OutputType.FILE);
        try {
            //save the screenshot taken in destination path
            FileUtils.copyFile(file, new File("./ScreenShot_Folder/" + name + ".png"));
        } catch (
                IOException e) {
            e.printStackTrace();
        }
    }
}
