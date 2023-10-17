package assertions;

import example.ExampleUnit;
import org.testng.annotations.Test;

import static org.testng.Assert.assertFalse;
import static org.testng.Assert.assertTrue;

public class AssertTrueFalseTest {
    ExampleUnit myUnit = new ExampleUnit();

    @Test
    public void testGetTheBooleanTrue() {
        assertTrue(myUnit.getTheBoolean());
    }

    @Test
    public void testGetTheBooleanFalse() {
        assertFalse(myUnit.getTheBoolean());
    }
}
