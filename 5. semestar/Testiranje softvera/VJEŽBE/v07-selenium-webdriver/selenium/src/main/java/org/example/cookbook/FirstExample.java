package org.example.cookbook;

import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;

public class FirstExample {

	WebDriver driver;

	/**
	 * This method will be executed before the test start.
	 */
	@BeforeSuite
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

		// Wait 5 seconds for loading the page before Exception
		driver.manage().timeouts().pageLoadTimeout(5, TimeUnit.SECONDS);
		
		// Wait 1 second before very action
		driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
		
		// Navigate to the required web page 
		driver.navigate().to("https://www.google.com");
		
	}

	@Test
	public void search() {

		// Locate element by value of its NAME attribute
		WebElement test = driver.findElement(By.name("q"));
		
		// Enter text 
		test.sendKeys("FTN informatika");
		
		// Press ENTER key on keyboard
		test.sendKeys(Keys.ENTER);

	}

	@Test(dependsOnMethods = { "search" })
	public void clickFirstLink() {
		
		// Locate element by XPATH selector
		WebElement ftnInformatika = driver.findElement(By.xpath("//h3[text()='FTN Informatika: Kursevi Programiranja Novi Sad']"));
		
		// Click on element
		ftnInformatika.click();
		
		// driver navigation function
		driver.navigate().back();
        driver.navigate().forward();
        driver.navigate().refresh();
	}

	/**
	 * This method will be executed at the end of the test.
	 */
	@AfterSuite
	public void quitDriver() {
		
		// Close browser window
		driver.quit();
	}

}
