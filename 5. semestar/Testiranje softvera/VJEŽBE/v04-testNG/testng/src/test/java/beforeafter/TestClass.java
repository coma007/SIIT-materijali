package beforeafter;

import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterGroups;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeGroups;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class TestClass {
    /**
     * Before suite method which is executed before
     * starting of any of the test in the suite.
     */
    @BeforeSuite
    public void beforeSuite(){
        System.out.println("Before Suite method");
    }

     /** After suite method which gets executed after
    * execution of all the tests in a suite.
            */
    @AfterSuite
    public void afterSuite(){
        System.out.println("After Suite method");
    }

    /**
     * Before Test method which gets executed before the first
     * test-method mentioned in each test inside the 'test'
     * tag in test suite.
     */
     @BeforeTest
     public void beforeTest(){
     System.out.println("Before Test method");
     }

     /**
      * After Test method which gets executed after
      * the last test-method
     */
    @AfterTest
    public void afterTest(){
        System.out.println("After Test method");
    }

    /**
     * Before Class method which gets executed before
     * any of the test-methods inside a class.
     */
    @BeforeClass
    public void beforeClass(){
        System.out.println("Before Class method");
    }

    /**
     * After Class method which gets executed after
     * all of the test-methods inside a class gets executed.
     */
    @AfterClass
    public void afterClass(){
        System.out.println("After Class method");
    }

    /**
     * Before group method gets executed before executing any of
     * the tests belonging to the group as mentioned in the 'groups'
     * attribute.
     * The following method gets executed before execution of the
     * test-method belonging to group "testOne".
     */
    @BeforeGroups(groups={"testOne"})
    public void beforeGroupOne(){
        System.out.println("Before Group Test One method");
    }

    /**
     * After group method gets executed after executing all the
     * tests belonging to the group as mentioned in the 'groups'
     * attribute.
     * The following method gets executed after execution of the
     * test-methods belonging to group "testOne".
     */
    @AfterGroups(groups={"testOne"})
    public void afterGroupOne(){
        System.out.println("After Group Test One method");
    }

    /**
     * Before group method gets executed before executing any of the
     tests
     * belonging to the group as mentioned in the 'groups' attribute.
     * The following method gets executed before execution of the
     * test-method belonging to group "testTwo".
     */
    @BeforeGroups(groups={"testTwo"})
    public void beforeGroupTwo(){
        System.out.println("Before Group Test two method");
    }

    /**
     * After group method gets executed after executing all the tests
     * belonging to the group as mentioned in the 'groups' attribute.
     * The following method gets executed after execution of the
     * test-methods belonging to group "testTwo".
     */
    @AfterGroups(groups={"testTwo"})
    public void afterGroupTwo(){
        System.out.println("After Group Test two method");
    }

    /**
     * Before method which gets executed before each test-method.
     */
    @BeforeMethod
    public void beforeMethod(){
        System.out.println("Before Method");
    }

    /**
     * After method which gets executed after each test-method.
     */
    @AfterMethod
    public void afterMethod(){
        System.out.println("After Method");
    }

    /**
     * Test-method which belongs to group "testOne".
     */
    @Test(groups={"testOne"})
    public void testOneMethod(){
        System.out.println("Test one method");
    }

    /**
     * Test-method which belongs to group "testTwo".
     */
    @Test(groups={"testTwo"})
    public void testTwoMethod(){
        System.out.println("Test two method");
    }
}
