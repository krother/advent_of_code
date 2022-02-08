import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    @Test
    public void testGiftWrap() {
        Solution s = new Solution();
        assertEquals(58, s.wrap("2x3x4"));
        assertEquals(43, s.wrap("1x1x10"));
    }

    @Test
    public void testSolve() {
        Solution s = new Solution();
        assertEquals(101, s.solve("2x3x4\n1x1x10"));
    }

}
