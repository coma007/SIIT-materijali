package assertions;

import example.ExampleUnit;
import org.testng.annotations.Test;

import static org.testng.Assert.assertNotSame;
import static org.testng.Assert.assertSame;

public class AssertSameNotSameTest {
    ExampleUnit myUnit = new ExampleUnit();

    @Test
    public void testGetTheSameObjectSame() {

        ExampleUnit myUnit2 = new ExampleUnit();

        assertNotSame(myUnit, myUnit2);

        myUnit2 = myUnit;
        assertSame(myUnit, myUnit2);
    }

    @Test
    public void testSameString() {
        assertSame("testing", "testing");
        assertNotSame("testing", new String("testing"));
    }
}
