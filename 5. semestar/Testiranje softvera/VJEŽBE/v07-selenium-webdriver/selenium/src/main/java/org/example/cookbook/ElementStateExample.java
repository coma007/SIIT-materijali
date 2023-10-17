package org.example.cookbook;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

public class ElementStateExample {

	WebDriver driver;

	@BeforeClass
	public void setup() {

		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

	}

	@BeforeMethod
	public void navigate() {
		driver.get("http://demo-store.seleniumacademy.com/");
	}

	@Test
	public void elementGetAttributesExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		System.out.println("Name of the box is: " + searchBox.getAttribute("name"));

		System.out.println("Id of the box is: " + searchBox.getAttribute("id"));

		System.out.println("Class of the box is: " + searchBox.getAttribute("class"));

		System.out.println("Placeholder of the box is: " + searchBox.getAttribute("placeholder"));
	}

	@Test
	public void elementGetCssValueExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		System.out.println("Font of the box is: " + searchBox.getCssValue("font-family"));
	}

	@Test
	public void elementLocationAndSizeExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		System.out.println("Location of the box is: " + searchBox.getLocation());

		System.out.println("Size of the box is: " + searchBox.getSize());
	}

	@Test
	public void elementGetTextExample() {

		WebElement siteNotice = driver.findElement(By.className("global-site-notice"));

		System.out.println("Complete text is: " + siteNotice.getText());
	}

	@Test
	public void elementGetTagNameExample() {

		WebElement searchButton = driver.findElement(By.className("search-button"));

		System.out.println("Html tag of the button is: " + searchButton.getTagName());
	}
	
	@Test
	public void elementSendKeysExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		searchBox.sendKeys("Phones");
		searchBox.submit();

		assertThat(driver.getTitle()).isEqualTo("Search results for: 'Phones'");
	}

	@Test
	public void elementSendKeysCompositeExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		searchBox.sendKeys(Keys.chord(Keys.SHIFT, "phones"));
		searchBox.submit();

		assertThat(driver.getTitle()).isEqualTo("Search results for: 'PHONES'");
	}

	@Test
	public void elementClearExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		searchBox.sendKeys(Keys.chord(Keys.SHIFT, "phones"));
		searchBox.clear();
	}

	@Test
	public void elementSubmitExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		searchBox.sendKeys(Keys.chord(Keys.SHIFT, "phones"));
		searchBox.submit();
	}

	@Test
	public void elementStateExample() {

		WebElement searchBox = driver.findElement(By.name("q"));

		System.out.println("Search button is displayed: " + searchBox.isDisplayed());

		System.out.println("Search button is enabled: " + searchBox.isEnabled());

		System.out.println("Search button is selected: " + searchBox.isSelected());
	}

	@AfterClass
	public void tearDown() {
		driver.quit();
	}
}