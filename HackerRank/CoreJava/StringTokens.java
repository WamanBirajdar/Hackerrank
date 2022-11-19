

package StringExample;

import java.util.StringTokenizer;

public class String_Example {

	public static void main(String[] args) {
		String name="waman birajdar";
		
		StringTokenizer str = new StringTokenizer(name, " .,'?!_@");
        System.out.println(str.countTokens());
        while (str.hasMoreTokens()) {
            System.out.println(str.nextToken());
        }
		
		

	}

}

