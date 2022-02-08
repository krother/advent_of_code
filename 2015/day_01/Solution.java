import java.io.BufferedReader;
import java.io.FileReader;

public class Solution {

    public int solve1(String filename) throws Exception {
        BufferedReader b = new BufferedReader(new FileReader(filename));
        String s = b.readLine();
        System.out.println(s);
        return 42;
    }

    public static void main(String[] args) throws Exception {

        Solution s = new Solution();
        System.out.println(s.solve1("/home/kristian/projects/advent_of_code/2015/day_01/input_data.txt"));
    }
}
