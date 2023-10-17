package junit5tests;

import org.junit.jupiter.params.provider.Arguments;

import java.util.stream.Stream;

import static org.junit.jupiter.params.provider.Arguments.arguments;

public class ParamProvider {

    static Stream<Arguments> sourceStream_StringDouble() {
        return Stream.of(arguments("apple", 8.9), arguments("pear", 1.9));
    }
}
