package org.example.cookbook;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

public class Exercise1 {
	WebDriver driver;

	/**
	 * This method will be executed before the test start.
	 */
	@BeforeSuite
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

		// Configure browser if required
		// Maximize browser window
		driver.manage().window().maximize();

		// Wait 5 seconds for loading the page before Exception
		driver.manage().timeouts().pageLoadTimeout(5, TimeUnit.SECONDS);

		// Wait 1 second before very action
		driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);

		// Navigate to the required web page
		driver.navigate().to("http://www.calculator.net/");

	}

	@Test
	public void calculate() {

		// Choose percentage calculator with XPATH selector
		driver.findElement(By.xpath("//*[@id=\"hl3\"]/li[3]/a")).click();

		// Locate element by value of its ID attribute
		WebElement percentageValue = driver.findElement(By.id("cpar1"));

		// Enter value at element
		// ATTENTION: sendKeys always receives STRING value!!!
		percentageValue.sendKeys("10");

		// Same thing, but in one line
		driver.findElement(By.id("cpar2")).sendKeys("50");

		// Locate element by XPATH and click on it
		driver.findElement(By.xpath(".//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]")).click();

		// Locate element by CSS selector
		WebElement resultElement = driver.findElement(By.cssSelector("#content > p.verybigtext > font > b"));

		// Get text from WebElement
		String resultValue = resultElement.getText();

		// Same as above in one line
		// String resultValue = driver.findElement(By.cssSelector("#content >
		// p.verybigtext > font > b")).getText();

		// Print result in Java console
		System.out.println(" The Result is " + resultValue);

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
