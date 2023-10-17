package org.example.cookbook;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class InteractionExample2 {
	WebDriver driver;

	/**
	 * This method will be executed before the test start.
	 */
	@BeforeClass
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

	}

	@Test
	public void shouldDrag() {

		driver.get("http://guidebook.seleniumacademy.com/DragMe.html");

		WebElement dragMe = driver.findElement(By.id("draggable"));

		Actions actions = new Actions(driver);
		actions.dragAndDropBy(dragMe, 300, 200).perform();
	}

	@Test
	public void shouldDragAndDrop() {

		driver.get("http://guidebook.seleniumacademy.com/DragAndDrop.html");

		WebElement src = driver.findElement(By.id("draggable"));
		WebElement trgt = driver.findElement(By.id("droppable"));

		Actions actions = new Actions(driver);
		actions.dragAndDrop(src, trgt).perform();
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
