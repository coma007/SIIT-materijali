package org.example.cookbook;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

public class InteractionExample4 {
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
	public void shouldMoveByOffSetAndClick() {

		driver.get("http://guidebook.seleniumacademy.com/Selectable.html");

		WebElement seven = driver.findElement(By.name("seven"));
		System.out.println(
				"X coordinate: " + seven.getLocation().getX() + ", Y coordinate: " + seven.getLocation().getY());

		Actions actions = new Actions(driver);
		actions.moveByOffset(seven.getLocation().getX() + 150, seven.getLocation().getY() + 1).click();
		actions.perform();
	}

	@Test
	public void shouldMoveByOffSetAndClickMultiple() {

		driver.get("http://guidebook.seleniumacademy.com/Selectable.html");

		WebElement one = driver.findElement(By.name("one"));
		WebElement eleven = driver.findElement(By.name("eleven"));
		WebElement five = driver.findElement(By.name("five"));

		int border = 1;
		int tileWidth = 100;
		int tileHeight = 80;

		Actions actions = new Actions(driver);

		// Click on One
		actions.moveByOffset(one.getLocation().getX() + border, one.getLocation().getY() + border).click();
		actions.build().perform();

		// Click on Eleven
		actions.moveByOffset(2 * tileWidth + 4 * border, 2 * tileHeight + 4 * border).click();
		actions.build().perform();

		// Click on Five
		actions.moveByOffset(-2 * tileWidth - 4 * border, -tileHeight - 2 * border).click();
		actions.build().perform();
	}

	@Test
	public void shouldClickOnElement() {

		driver.get("http://guidebook.seleniumacademy.com/Selectable.html");

		WebElement one = driver.findElement(By.name("one"));
		WebElement eleven = driver.findElement(By.name("eleven"));
		WebElement five = driver.findElement(By.name("five"));

		Actions actions = new Actions(driver);
		actions.click(one).click(eleven).click(five).build().perform();
	}

	@Test
	public void shouldClickAndHold() {

		driver.get("http://guidebook.seleniumacademy.com/Sortable.html");

		Actions actions = new Actions(driver);

		// Move tile3 to the position of tile2
		actions.moveByOffset(200, 20).clickAndHold().moveByOffset(120, 0).perform();
	}

	@Test
	public void shouldClickAndHoldElement() {

		driver.get("http://guidebook.seleniumacademy.com/Sortable.html");

		Actions actions = new Actions(driver);
		WebElement three = driver.findElement(By.name("three"));

		// Move tile3 to the position of tile2
		actions.clickAndHold(three).moveByOffset(120, 0).perform();
	}

	@Test
	public void shouldClickAndHoldAndRelease() {

		driver.get("http://guidebook.seleniumacademy.com/Sortable.html");

		WebElement three = driver.findElement(By.name("three"));
		Actions actions = new Actions(driver);

		// Move tile3 to the position of tile2
		actions.clickAndHold(three).moveByOffset(120, 0).release().perform();
	}

	@Test
	public void shouldClickAndHoldAndReleaseOnElement() {

		driver.get("http://guidebook.seleniumacademy.com/Sortable.html");

		WebElement three = driver.findElement(By.name("three"));
		WebElement two = driver.findElement(By.name("two"));
		Actions actions = new Actions(driver);

		// Move tile3 to the position of tile2
		actions.clickAndHold(three).release(two).perform();
	}

	@Test
	public void shouldDoubleClick() {

		driver.get("http://guidebook.seleniumacademy.com/DoubleClick.html");

		WebElement dblClick = driver.findElement(By.name("dblClick"));
		Actions actions = new Actions(driver);
		actions.moveToElement(dblClick).doubleClick().perform();
	}

	@Test
	public void shouldDoubleClickElement() {

		driver.get("http://guidebook.seleniumacademy.com/DoubleClick.html");

		WebElement dblClick = driver.findElement(By.name("dblClick"));
		Actions actions = new Actions(driver);
		actions.doubleClick(dblClick).perform();
	}

	@Test
	public void shouldContextClick() throws InterruptedException {

		driver.get("http://guidebook.seleniumacademy.com/ContextClick.html");

		WebElement contextMenu = driver.findElement(By.id("div-context"));
		Actions actions = new Actions(driver);
		actions.contextClick(contextMenu).click(driver.findElement(By.name("Item 4"))).perform();

		// Switch to the alert box and click on OK button
		Alert alert = driver.switchTo().alert();

		System.out.println("Alert Text\n" + alert.getText());

		Thread.sleep(2000);
		alert.accept();

	}

	@Test
	public void shouldContextClickAtCurrentLocation() {

		driver.get("http://guidebook.seleniumacademy.com/ContextClick.html");

		WebElement contextMenu = driver.findElement(By.id("div-context"));
		Actions actions = new Actions(driver);
		actions.moveToElement(contextMenu).contextClick().click(driver.findElement(By.name("Item 4"))).perform();
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
