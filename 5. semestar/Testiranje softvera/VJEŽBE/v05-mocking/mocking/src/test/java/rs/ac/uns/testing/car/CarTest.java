package rs.ac.uns.testing.car;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import rs.ac.uns.testing.car.Car;

import static org.testng.Assert.assertEquals;

public class CarTest {
    Car test_car;

    @BeforeMethod
    public void createCarObject() {
        test_car = new Car("Toyota", "Prius", 10, 50);
    }

    //TODO: constructor sets gasTankLevel properly
    @Test
    public void testInitialGasTank() {
        assertEquals(test_car.getGasTankLevel(), 10,.001);
    }

    //TODO: gasTankLevel is accurate after driving within tank range
    @Test
    public void testGasTankAfterDriving() {
        test_car.drive(50);
        assertEquals(9, test_car.getGasTankLevel(),.001);
    }

    //TODO: gasTankLevel is accurate after attempting to drive past tank range
    //TODO: can't have more gas than tank size, expect an exception
}
