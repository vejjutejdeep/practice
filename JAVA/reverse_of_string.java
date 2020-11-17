/*package whatever //do not write package name here */

import java.util.*;

class GFG {
    public static String reverse(String word) {
        String rword = "";
        for (int ele = 0; ele < word.length(); ele++) {
            rword = word.charAt(ele) + rword;
        }
        return rword;
    }

    public static void main(String[] args) {
        // code
        Scanner scan = new Scanner(System.in);
        int test = Integer.parseInt(scan.nextLine());
        for (int ele = 0; ele < test; ele++) {
            String word = scan.nextLine();
            System.out.println(reverse(word));
        }
        scan.close();
    }
}