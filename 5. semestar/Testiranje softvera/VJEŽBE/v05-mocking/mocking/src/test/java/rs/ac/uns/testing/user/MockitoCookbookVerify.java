package rs.ac.uns.testing.user;

import org.mockito.InOrder;
import org.testng.annotations.Test;

import static org.mockito.Mockito.*;

public class MockitoCookbookVerify {

    @Test
    public void exampleVerify() {
        PasswordEncoder mPasswordEncoder = mock(PasswordEncoder.class);

        when(mPasswordEncoder.encode("a")).thenReturn("1");
        mPasswordEncoder.encode("a");

        verify(mPasswordEncoder).encode("a");

        // this one will fail
        // verify(mPasswordEncoder).encode("b");

        // this one will pass
        verify(mPasswordEncoder).encode(anyString());
    }

    @Test
    public void exampleVerifyMultipleCalls() {
        PasswordEncoder mPasswordEncoder = mock(PasswordEncoder.class);
        when(mPasswordEncoder.encode("a")).thenReturn("1");
        mPasswordEncoder.encode("a");

        // verify the exact number of invocations
        // verify(mPasswordEncoder, times(42)).encode(anyString());

        // verify that there was at least one invocation
        verify(mPasswordEncoder, atLeastOnce()).encode(anyString());

        // verify that there were at least five invocations
        // verify(mPasswordEncoder, atLeast(5)).encode(anyString());

        // verify the maximum number of invocations
        verify(mPasswordEncoder, atMost(5)).encode(anyString());

        // verify that it was the only invocation and
        // that there're no more unverified interactions
        verify(mPasswordEncoder, only()).encode(anyString());

        // verify that there were no invocations
        // verify(mPasswordEncoder, never()).encode(anyString());
    }

    @Test
    public void exampleCallOrder() {
        PasswordEncoder first = mock(PasswordEncoder.class);
        PasswordEncoder second = mock(PasswordEncoder.class);

        // simulate calls
        first.encode("f1");
        second.encode("s1");
        first.encode("f2");

        // verify call order
        InOrder inOrder = inOrder(first, second);
        inOrder.verify(first).encode("f1");
        inOrder.verify(second).encode("s1");
        inOrder.verify(first).encode("f2");

        // If we rearrange the order of the simulated calls, the test will fail with VerificationInOrderFailure.
        // InOrder inOrder2 = inOrder(first, second);
        // inOrder2.verify(first).encode("f2");
        // inOrder2.verify(second).encode("s1");
    }
}
