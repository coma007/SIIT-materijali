package rs.ac.uns.testing.user;

import org.mockito.Mockito;
import org.testng.annotations.Test;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.testng.AssertJUnit.assertEquals;

public class MockitoSpy {

    @Test
    public void exampleSpy() {
        Demo sDemo = Mockito.spy(new Demo());

        // if not stubbed, spy will call real method
        assertEquals(1, sDemo.returnOne());

        // spy objects can be verified
        verify(sDemo).returnOne();

        // stubbing spy
        when(sDemo.returnOne()).thenReturn(5);
        assertEquals(5, sDemo.returnOne());
    }
}

class Demo {
    public int returnOne() {
        return 1;
    }
}
