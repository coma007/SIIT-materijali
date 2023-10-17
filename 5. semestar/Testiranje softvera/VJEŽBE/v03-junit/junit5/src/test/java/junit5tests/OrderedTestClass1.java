package junit5tests;

import org.junit.jupiter.api.*;

@TestMethodOrder(MethodOrderer.MethodName.class)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class OrderedTestClass1 {

    @BeforeAll
    void beforeAll() {
        System.out.println("--This is the before All method");
    }

    @BeforeEach
    void beforeEach() {
        System.out.println("----This is the before Each method");
    }

    @AfterAll
    void afterAll() {
        System.out.println("--This is the after All method");
    }

    @AfterEach
    void afterEach() {
        System.out.println("----This is the after Each method");
    }

    @Test
    void firstMethod() {
        System.out.println("This is the first test method");
    }

    @Test
    @DisplayName("US1234 - TC12 - this method is the second one")
    void secondMethod() {
        System.out.println("This is the second test method");
    }

    @Test
    @DisplayName("A display name")
    void thirdTest() {
        System.out.println("This is the third test method");
    }
}
