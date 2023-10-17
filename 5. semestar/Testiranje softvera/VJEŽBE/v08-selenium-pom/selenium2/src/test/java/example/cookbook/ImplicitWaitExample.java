package example.cookbook;

import java.util.List;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class ImplicitWaitExample {

	private WebDriver driver;

	@BeforeMethod
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

		// Configure browser if required
		// Maximize browser window
		driver.manage().window().maximize();

		// Wait 10 seconds before very action
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

		// Navigate to the required web page
		driver.navigate().to("http://www.google.com");

	}

	@Test
	public void implicit() {
//		WebElement element = driver.findElement(By.name("non-existing-element"));
		WebElement element = driver.findElement(By.name("q"));
		element.sendKeys("Selenium WebDriver Interview questions");
		element.sendKeys(Keys.RETURN);
		
		List<WebElement> list = driver.findElements(By.className("_Rm"));
		System.out.println(list.size());
	}

	@AfterMethod
	public void tearDown() throws Exception {
		driver.quit();
	}
}
