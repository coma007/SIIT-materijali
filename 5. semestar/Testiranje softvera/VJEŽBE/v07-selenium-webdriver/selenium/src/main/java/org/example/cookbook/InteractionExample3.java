package org.example.cookbook;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Action;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

public class InteractionExample3 {
	WebDriver driver;

	/**
	 * This method will be executed before the test start.
	 */
	@BeforeSuite
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();
	}

	@Test
	public void shouldPerformCompositeAction() {

		driver.get("http://guidebook.seleniumacademy.com/Selectable.html");

		WebElement one = driver.findElement(By.name("one"));
		WebElement three = driver.findElement(By.name("three"));
		WebElement five = driver.findElement(By.name("five"));

		// Add all the actions into the Actions actions.
		Actions actions = new Actions(driver);
		actions.keyDown(Keys.CONTROL).click(one).click(three).click(five).keyUp(Keys.CONTROL);

		// Generate the composite action.
		Action compositeAction = actions.build();

		// Perform the composite action.
		compositeAction.perform();
	}

	@Test
	public void shouldPerformAction() {
		
		driver.navigate().to("https://www.google.com");

		// Locate element by value of its NAME attribute
		WebElement input = driver.findElement(By.name("q"));

		// Enter text
		Actions builder = new Actions(driver);

		builder.moveToElement(input).click().keyDown(input, Keys.SHIFT).sendKeys(input, "please turn off caps lock")
				.keyUp(input, Keys.SHIFT).perform();

		// Press ENTER key on keyboard
		input.sendKeys(Keys.ENTER);

	}

	/**
	 * This method will be executed at the end of the test.
	 */
	@AfterSuite
	public void quitDriver() {

		// Close browser window
		driver.quit();
		driver = null;
	}
}
