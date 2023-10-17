package org.example.tests;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

import static org.testng.Assert.assertEquals;

public class LoginTest {
    private WebDriver driver;

    static final String USERNAME = "sladakovic.sv18.2020@uns.ac.rs";
    static final String PASSWORD = "12.3 torustorus";
    static final String COURSE_NAME = "Testiranje softvera";
//    static final String COURSE_NAME = "Testiranje softvera";

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
        driver = new ChromeDriver();

        //define the url
        driver.get("https://login.uns.ac.rs/ftn-canvas/login?SAMLRequest=fZJBT8MwDIXv%2FIoq97RrVtYRtZXGJsSkAdU2OHBBWZdukVpnxOmAf0%2FaghiXXu33PdsvSVDU1YnPGnuEtXxvJFrvs64AeddISWOAa4EKOYhaIrcF38weVpz5I34y2upCV%2BQCGSYEojRWaSDecpGSt%2FEknk7KEaNxHE5pFJUlFWE0prGIxE04La53QhLvRRp0TEqchQMRG7kEtAKsK40Yo2FIWbxlIWcTzuJX4i3cHQqE7aijtSfkQVDpgwK%2FAfRF4RsMSgu0EHAW2LeIN%2Ftdb64Bm1qajTRnVcjn9erPpkd8R194dQZBGwDx8p9YbhXsFRyGE9n1IuT3221O86fNlmRJ68O7O002OLYVsiS41Cf9iz66SctFritVfHl32tTCDi%2FSVtSelp2UWyMAlQTrQqkq%2FTE3UliZEmsaSYKsH%2Fn%2F32RX3w%3D%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=qrDREzBhnsJlpjenEJUriQi7lOKR5XiA0F7PM9Lfu%2Bjmy5nNE3Qv8ujGGPJsCyOlPh%2B5%2FWtKbxvOcQraaoa91L7fiTRZulA0d06n5Jo73jpse07RSLhnV3J9%2B37rbJMshq%2Ba%2BfjguoPpeBxqrFz%2BWYq%2FLOFeB5jILly5zxSTwhPlIzuW%2BlH9zlSPlHdVU9mpXgoQp4%2B0fR71Tqbm7DovZXOra5it2PxjLN%2BPLPkWAfyZcmcRWs55D9QC%2B5zkQXsKcTjIDY9lrUWCFR2K1Hk%2Bt7CFUj5tKuOjTKGJmxpK2DT2IIeCSgnLGAh%2BxbxmsUlMKMLHgfM%2BWj%2BdLV6Mg22iSg%3D%3D");

        //maximize the window
        driver.manage().window().maximize();

        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        //get the title of the webpage
        String pageTitle = driver.getTitle();
        System.out.println("The title of this page is ===> " +pageTitle);
    }

    @Test
    public void loginTest() throws InterruptedException {

        //enter the locator of username and clear the input field before entering any value
        driver.findElement(By.name("username")).clear();

        //enter the username
        driver.findElement(By.name("username")).sendKeys(USERNAME);

        //enter the locator of continue button and click
        driver.findElement(By.name("login")).click();

        //enter the locator of password and clear the input field
        driver.findElement(By.name("passwd")).clear();

        //enter the value of password
        driver.findElement(By.name("passwd")).sendKeys(PASSWORD);

        //enter the locator of login button and click
        driver.findElement(By.name("pass")).click();

        //wait for the page to load
        Thread.sleep(2000);

        // assert login
        assertEquals(driver.getTitle(), "Dashboard");

        //downcast the driver to access TakesScreenshot method
        TakesScreenshot ts = (TakesScreenshot)driver;

        //capture screenshot as output type FILE
        File file = ts.getScreenshotAs(OutputType.FILE);
        try {
            //save the screenshot taken in destination path
            FileUtils.copyFile(file, new File("./ScreenShot_Folder/Test1_Login.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("the login page screenshot is taken");
    }

    @Test(dependsOnMethods = "loginTest")
    public void searchCourseTest() {
        // click courses button
        driver.findElement(By.id("global_nav_courses_link")).click();

        // search current course
        driver.findElement(By.linkText(COURSE_NAME)).click();

        // assert course page
        assertEquals(driver.getTitle(), COURSE_NAME);

        TakesScreenshot ts1 = (TakesScreenshot)driver;
        File file1 = ts1.getScreenshotAs(OutputType.FILE);

        try {
            FileUtils.copyFile(file1, new File("./ScreenShot_Folder/Test2_CoursePage.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // TODO: assert your name in list of People

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
