import java.io.BufferedReader;
import java.io.FileReader;

public class Solution {

    public int wrap(String size) {

        String[] present = size.split("x");

        int[] present_size = new int[3];
        int largest = 0;

        for (int i=0; i<3; i++) {
            present_size[i] = Integer.parseInt(present[i]);
            if (present_size[i] > largest) largest = present_size[i];
        }
        int l = present_size[0];
        int w = present_size[1];
        int h = present_size[2];
        int area = 2 * l * w  // 12
                 + 2 * w * h  // 24
                 + 2 * l * h; // 16

        area += l * w * h / largest;

        return area;
    }

    public int solve(String presents) {
        int result = 0;
        String[] items = presents.split("\n");
        for (int i=0; i<items.length; i++) {
            result += wrap(items[i]);
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        String filename = "input_data.txt";
        BufferedReader b = new BufferedReader(new FileReader(filename));
        String line = b.readLine();;
        String data = "";
        while (line != null) {
            data += line;
            line = b.readLine();
        }
        Solution s = new Solution();
        System.out.println(s.solve(data));
        // should be 1598415
    }
}
