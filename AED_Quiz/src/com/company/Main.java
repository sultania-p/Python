package practice;

import java.util.ArrayList;
import java.util.Collections;

public class Test() {

    public static void main(String[] args) {

        int[] myArray={12,3,10,2,4} ;
        ArrayList<Integer>evenList = new ArrayList<Integer>();

        for(int i=0;i<myArray.length;i++){
            if(myArray[i]%2==0){
                evenList.add(myArray[i]);
            }
        }
        System.out.print(evenList);
    }

}
