package rs.ac.uns.testing.user;

import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.ArrayList;

import static org.mockito.Mockito.*;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotEquals;

public class MockitoCookbook {

    private PasswordEncoder mPasswordEncoder;

    @Mock
    private PasswordEncoder mPasswordEncoderAnotation;

    @BeforeMethod
    public void setUp() throws Exception {

        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void exampleWithoutStubbing() {
        mPasswordEncoder = Mockito.mock(PasswordEncoder.class);

        // there is no stubbing, passwordEncoder is mocked, so real implementation cant be called
        assertEquals(mPasswordEncoder.encode("1"), null);
    }

    @Test
    public void exampleWhenThen() {
        mPasswordEncoder = Mockito.mock(PasswordEncoder.class);

        when(mPasswordEncoder.encode("1")).thenReturn("a");

        assertEquals(mPasswordEncoder.encode("1"), "a");
    }

    @Test
    public void exampleDoWhen() {
        mPasswordEncoder = Mockito.mock(PasswordEncoder.class);

        doReturn("a").when(mPasswordEncoder).encode("1");

        assertEquals(mPasswordEncoder.encode("1"), "a");
    }

    @Test
    public void exampleMultipleCalls() {

        // this example uses passwordEncoder created using @Mock annotation
        // be aware of MockitoAnnotations.openMocks(this);
        when(mPasswordEncoderAnotation.encode("1")).thenReturn("a", "b");

        // when(mPasswordEncoderAnotation.encode("1")).thenReturn("a").thenReturn("b");

        // doReturn("a", "b").when(mPasswordEncoderAnotation).encode("1");

        // first execution
        assertEquals(mPasswordEncoderAnotation.encode("1"), "a");

        // second execution
        assertEquals(mPasswordEncoderAnotation.encode("1"), "b");

        // the last value will be used as a result for all further method calls
        assertEquals(mPasswordEncoderAnotation.encode("1"), "b");
    }

    @Test(expectedExceptions = IllegalArgumentException.class)
    public void exampleThrowException() {
        mPasswordEncoder = Mockito.mock(PasswordEncoder.class);

        when(mPasswordEncoder.encode("1")).thenAnswer(invocation -> {
            throw new IllegalArgumentException();
        });

        // when(mPasswordEncoder.encode("1")).thenThrow(IllegalArgumentException.class);

        // doThrow(IllegalArgumentException.class).when(mPasswordEncoder.encode("1"));

        mPasswordEncoder.encode("1");
    }

    @Test
    public void exampleRealMethodCall() {
        ArrayList<String> mList = Mockito.mock(ArrayList.class);

        when(mList.size()).thenReturn(5);
        assertEquals(mList.size(), 5);

        when(mList.size()).thenCallRealMethod();
        assertNotEquals(mList.size(), 5);

    }

}
