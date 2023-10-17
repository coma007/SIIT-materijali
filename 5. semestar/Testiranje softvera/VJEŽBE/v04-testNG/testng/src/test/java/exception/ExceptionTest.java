package exception;

import java.io.IOException;
import org.testng.annotations.Test;
public class ExceptionTest {

    @Test(expectedExceptions={IOException.class})
    public void exceptionTestOne() throws Exception{
        throw new IOException();
    }

    @Test(expectedExceptions={IOException.class,
            NullPointerException.class})
    public void exceptionTestTwo() throws Exception{
        throw new Exception();
    }
}
