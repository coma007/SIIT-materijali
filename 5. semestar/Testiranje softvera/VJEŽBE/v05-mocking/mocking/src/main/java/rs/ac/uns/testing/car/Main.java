package rs.ac.uns.testing.car;

public class Main {

    public static void main(String[] args) {
        Car car = new Car("Toyota", "Prius", 10, 50);
        System.out.println(car.getMake() + " - " + car.getModel());
        car.drive(1000);
        System.out.println(car.getOdometer());
    }
}
