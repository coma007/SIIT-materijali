package example.tests;

import example.helper.Helper;
import example.pages.FreelaancerApplyPage;
import example.pages.HomePage;
import org.testng.Assert;
import org.testng.annotations.Test;

import static org.testng.Assert.assertTrue;

public class ApplyAsDeveloperTest extends TestBase {

    static final String ROLE = "Developer";
    static final String EMAIL = "email";
    static final String FULL_NAME = "full name";
    static final String PASSWORD = "password";

    @Test
    public void applyAsDeveloper() {
        //Create object of HomePage Class
        HomePage home = new HomePage(driver);
        home.clickOnFreelancerApplyButton();

        //Create object of FreelancerApplyPage
        FreelaancerApplyPage applyPage = new FreelaancerApplyPage(driver);

        //Check if page is opened
        Assert.assertTrue(applyPage.isPageOpened());

        //Fill up data
        applyPage.clickOnApplyingAs();
        applyPage.chooseRole(ROLE);

        applyPage.setDeveloperEmail(EMAIL);
        applyPage.setDeveloperFullName(FULL_NAME);
        applyPage.setDeveloperPassword(PASSWORD);
        applyPage.setDeveloperPasswordConfirmation(PASSWORD);

        //Click on join
        //applyPage.clickOnJoin();

        Helper.takeScreenshoot(driver, "login_application_full");
    }
}
