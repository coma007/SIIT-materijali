package rs.ac.uns.testing.user;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;

import java.util.Dictionary;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.when;

// example is using JUnit 5 testing framework
public class MockitoCookbookArgumentMatcher {

    // object is mocked using annotation
    @Mock
    private PasswordEncoder mPasswordEncoder;

    @BeforeEach
    public void setUp() throws Exception {
        // init mock objects
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void exampleAnyString() {
        // when the password encoder is asked to encode any string, then return the string ‘exact.
        when(mPasswordEncoder.encode(anyString())).thenReturn("exact");

        assertEquals("exact", mPasswordEncoder.encode("1"));
        assertEquals("exact", mPasswordEncoder.encode("abc"));
    }

    @Test
    public void exampleMultipleParams() {
        AClass mock = Mockito.mock(AClass.class);
        //This doesn’t work.
        // when(mock.call("a", anyInt())).thenReturn(true);

        when(mock.call(eq("a"), anyInt())).thenReturn(true);
    }

    @Test
    public void exampleAnyObject() {
        AClass mock = Mockito.mock(AClass.class);
        Mockito.doNothing().when(mock).callWithObject(any(Long.class));
    }

}

abstract class AClass {
    public abstract boolean call(String s, int i);
    public abstract void callWithObject(Long obj);
}
