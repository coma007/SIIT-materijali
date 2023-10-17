package disable;

import org.testng.Assert;
import org.testng.annotations.Test;

public class DisabledEnabledTests {

    @Test
    void firstTest() {
        System.out.println("This is the first test method");
    }

    @Test(enabled = true)
    void secondTest() {
        System.out.println("This is the second test method");
    }

    @Test(enabled = false)
    void thirdTest() {
        System.out.println("This is the third test method");
    }

    @Test
    void fourthTest() {
        System.out.println("This is the fourth test method");
    }

    @Test
    void fifthTest() {
        System.out.println("This is the fifth test method");
    }
}
