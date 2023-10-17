package priority;

import org.testng.annotations.Test;

public class PriorityTest {

    @Test
    public void c_method() {
        System.out.println("I'm in method C");
    }

    @Test(priority=1)
    public void b_method() {
        System.out.println("I'm in method B");
    }

    @Test(priority = 100)
    public void a_method() {
        System.out.println("I'm in method A");
    }

    @Test
    public void e_method() {
        System.out.println("I'm in method E");
    }

    @Test
    public void d_method() {
        System.out.println("I'm in method D");
    }
}
