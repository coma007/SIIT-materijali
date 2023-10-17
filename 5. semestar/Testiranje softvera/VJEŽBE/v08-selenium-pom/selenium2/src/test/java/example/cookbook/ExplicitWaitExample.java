package example.cookbook;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class ExplicitWaitExample {

	private WebDriver driver;

	@BeforeMethod
	public void initalize() {

		// Create a Selenium WebDriver instance
		System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
		driver = new ChromeDriver();

		// Configure browser if required
		// Maximize browser window
		driver.manage().window().maximize();

	}

	@Test
	public void dynamicContent() {
		// Navigate to the required web page
		driver.navigate().to("http://the-internet.herokuapp.com/dynamic_loading/2");

		WebElement startBtn = driver.findElement(By.cssSelector("#start>button"));
		startBtn.click();

		WebDriverWait wait = new WebDriverWait(driver, 20);
		WebElement helloWorld = wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("#finish>h4")));
//		WebElement helloWorld = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#finish>h4")));

//		WebElement helloWorld = driver.findElement(By.cssSelector("#finish>h4"));

		System.out.println(helloWorld.getText());
	}
	
	@Test
	public void dynamicContent2() {
		// Navigate to the required web page
		driver.navigate().to("http://the-internet.herokuapp.com/dynamic_loading/1");

		WebElement startBtn = driver.findElement(By.cssSelector("#start>button"));
		startBtn.click();

		WebElement helloWorld = new WebDriverWait(driver, 20)
		        .until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#finish>h4")));

//		WebElement helloWorld = new WebDriverWait(driver, 20)
//				.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("#finish>h4")));
		
//		WebElement helloWorld = driver.findElement(By.cssSelector("#finish>h4"));

		System.out.println(helloWorld.getText());
	}

	@AfterMethod
	public void tearDown() throws Exception {
		driver.quit();
	}
}
