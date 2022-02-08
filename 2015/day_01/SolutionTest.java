import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @org.junit.jupiter.api.Test
    @org.junit.jupiter.api.DisplayName("Hello World works")
    void solve1() throws Exception {
        Solution s = new Solution();
        assertEquals(s.solve1("hello"), 42);
    }
}
