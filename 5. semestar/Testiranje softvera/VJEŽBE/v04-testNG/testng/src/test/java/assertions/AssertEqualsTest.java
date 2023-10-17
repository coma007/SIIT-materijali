package assertions;

import example.ExampleUnit;
import org.testng.annotations.Test;

import static org.testng.Assert.assertEquals;

public class AssertEqualsTest {

    @Test
    public void testConcatenate() {
        ExampleUnit myUnit = new ExampleUnit();

        String result = myUnit.concatenate("one", "two");

        assertEquals("onetwo", result);
    }
}
