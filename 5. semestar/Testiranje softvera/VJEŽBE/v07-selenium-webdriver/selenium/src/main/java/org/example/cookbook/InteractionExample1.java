package org.example.cookbook;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

/**
 * Example for: - text box interaction - radio button selection - dropdown
 * selection
 * 
 * @author minamedic
 *
 */
public class InteractionExample1 {
	WebDriver driver;

	/**
	 * This method will be executed before the test start.
	 */
	@BeforeClass
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
		driver.navigate().to("https://www.rentalcars.com/en/airport-rentals/");

	}

	@Test
	public void interaction() throws InterruptedException {

		Thread.sleep(3000);
		driver.findElement(By.id("onetrust-accept-btn-handler")).click();

		// Text Box interaction
		driver.findElement(By.id("ftsAutocomplete")).sendKeys("Novi Sad");

		// Checkbox interaction
		boolean checkboxStateBeforeClick = driver.findElement(By.id("driver-over-min-age")).isSelected();
		System.out.println("Is checkbox selected? " + checkboxStateBeforeClick);

		driver.findElement(By.id("driver-over-min-age")).click();

		boolean checkboxStateAfterClick = driver.findElement(By.id("driver-over-min-age")).isSelected();
		System.out.println("Is checkbox selected? " + checkboxStateAfterClick);

		// Drop down item selection - by visible text
		Select dropdownPickupHours = new Select(driver.findElement(By.name("puHour")));
		Thread.sleep(1000);
		dropdownPickupHours.selectByValue("8");

		// Drop down item selection - by visible text
		Select dropdownPickupMinutes = new Select(driver.findElement(By.name("puMinute")));
		Thread.sleep(1000);
		dropdownPickupMinutes.selectByVisibleText("45");

		// Drop down item selection - by index of each option, INDEX STARTS FROM 0
		Select dropdownDropOffMinutes = new Select(driver.findElement(By.name("doMinute")));
		Thread.sleep(1000);
		dropdownDropOffMinutes.selectByIndex(2);

		// Radio button selection
		driver.findElement(By.id("travel-reason-business")).click();

		// Click in Search button
		driver.findElement(By.id("formsubmit")).click();

	}

	/**
	 * This method will be executed at the end of the test.
	 */
	@AfterClass
	public void quitDriver() {

		// Close browser window
		driver.quit();
	}
}
