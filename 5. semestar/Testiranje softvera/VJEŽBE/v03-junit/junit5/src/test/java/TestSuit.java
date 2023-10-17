import org.junit.platform.suite.api.IncludeClassNamePatterns;
import org.junit.platform.suite.api.IncludeTags;
import org.junit.platform.suite.api.SelectPackages;
import org.junit.platform.suite.api.Suite;

@Suite
@SelectPackages( "junit5tests" )
@IncludeClassNamePatterns({"^.*Class?$"})
@IncludeTags("acceptance")
public class TestSuit {
}

