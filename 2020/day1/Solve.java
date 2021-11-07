/*

On Day 1, I wanted to go for a Java implementation.

Compile with

   javac Solve.java

Run with

   java Solve

*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;
import java.util.*;

class Solve {

   public static void main (String argv[]) throws IOException {

     // read a CSV file
     BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
     List<Integer> lines = new ArrayList<>();
     String line = null;
     while ((line = reader.readLine()) != null) {
        lines.add(Integer.parseInt(line));
     }

     int a, b, c, d;
     int size = lines.size();

     for (int i=0; i < size-2; i++) {
         a = lines.get(i);
         for (int j=i+1; j < size-1; j++) {
             b = lines.get(j);
             for (int k=j+1; k < size; k++) {
                 c = lines.get(k);
                 d = a + b + c;
                 if (d == 2020) {
                    System.out.println(a);
                    System.out.println(b);
                    System.out.println(c);
                    System.out.println(a * b * c);
                  }
            }
         }
     }
   }
}
