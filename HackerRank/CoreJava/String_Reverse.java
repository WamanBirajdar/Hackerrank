/*A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

code-->>

import java.io.*;
import java.util.*;*/

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        String B="";
        
        for(int i=0;i<A.length();i++)
        {
            B=A.charAt(i)+B;
        }
        System.out.println(A.equals(B)?"Yes":"No");
    }
}
