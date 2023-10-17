package example.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class FreelaancerApplyPage {

    private WebDriver driver;

    @FindBy(css = "div[data-role='custom_field']")
    WebElement applyingAs;

    @FindBy(css = "div[data-role='custom_select_options']")
    WebElement roles;

    @FindBy(tagName = "h1")
    WebElement heading;

    @FindBy(id="talent_create_applicant_email")
    WebElement developerEmail;

    @FindBy(id = "talent_create_applicant_password")
    WebElement developerPassword;

    @FindBy(id = "talent_create_applicant_password_confirmation")
    WebElement developerPasswordConfirmation;

    @FindBy(id = "talent_create_applicant_full_name")
    WebElement developerFullName;

    @FindBy(id ="save_new_talent_create_applicant")
    WebElement applyToptalButton;


    public FreelaancerApplyPage(WebDriver driver){
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public void clickOnApplyingAs() {
        applyingAs.click();
    }

    public void chooseRole(String role) {
        String locator = String.format(".//div[@data-role='custom_select_option_title'][text() = '%s']", role);
        roles.findElement(By.xpath(locator)).click();
    }

    public void setDeveloperEmail(String email){
        developerEmail.clear();
        developerEmail.sendKeys(email);
    }

    public void setDeveloperPassword(String password){
        developerPassword.clear();
        developerPassword.sendKeys(password);
    }

    public void  setDeveloperPasswordConfirmation(String passwordConfirmation){
        developerPasswordConfirmation.clear();
        developerPasswordConfirmation.sendKeys(passwordConfirmation);
    }

    public void setDeveloperFullName (String fullname){
        developerFullName.clear();
        developerFullName.sendKeys(fullname);
    }

    public void clickApplyToptalButton(){
        applyToptalButton.click();
    }

    public boolean isPageOpened(){
        boolean isOpened = (new WebDriverWait(driver, 10))
                .until(ExpectedConditions.textToBePresentInElement(heading, "Apply to Join\n" +
                        "the World's Top Talent Network"));

        return isOpened;
    }
}
