package org.example.cookbook;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.testng.Assert.assertEquals;

import java.util.List;

public class LocatorsExample {

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
    public void byIdLocatorExample() {

        WebElement searchBox = driver.findElement(By.id("search"));

        searchBox.sendKeys("Bags");
        searchBox.submit();

        assertThat(driver.getTitle())
                .isEqualTo("Search results for: 'Bags'");
    }

    @Test
    public void byClassNameLocatorExample() {

        WebElement searchBox = driver.findElement(By.id("search"));
        searchBox.sendKeys("Electronics");

        WebElement searchButton =
                driver.findElement(By.className("search-button"));
        searchButton.click();

        assertEquals(driver.getTitle(), "Search results for: 'Electronics'");
    }

    @Test
    public void byLinkTextLocatorExample() {

        WebElement myAccountLink =
                driver.findElement(By.linkText("MY ACCOUNT"));

        myAccountLink.click();

        assertThat(driver.getTitle())
                .isEqualTo("Customer Login");
    }

    @Test
    public void byPartialLinkTextLocatorExample() {

        WebElement orderAndReturns =
                driver.findElement(By.partialLinkText("PRIVACY"));

        orderAndReturns.click();

        assertThat(driver.getTitle())
                .isEqualTo("Privacy Policy");
    }

    @Test
    public void byTagNameLocatorExample() {

        // get all links from the Home page
        List<WebElement> links = driver.findElements(By.tagName("a"));

        System.out.println("Found links:" + links.size());

        // print links which have text using Java 8 Streams API
        for (WebElement link : links) {
			System.out.println(link.getText());
		}
    }

    @Test
    public void byXPathLocatorExample() {

        WebElement searchBox =
                driver.findElement(By.xpath("//*[@id='search']"));

        searchBox.sendKeys("Bags");
        searchBox.submit();

        assertThat(driver.getTitle())
                .isEqualTo("Search results for: 'Bags'");
    }

    @Test
    public void byCssSelectorLocatorExample() {

        WebElement searchBox =
                driver.findElement(By.cssSelector("#search"));

        searchBox.sendKeys("Bags");
        searchBox.submit();

        assertThat(driver.getTitle())
                .isEqualTo("Search results for: 'Bags'");
    }

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}

