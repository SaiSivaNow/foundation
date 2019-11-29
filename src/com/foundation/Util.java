package com.foundation;

import com.foundation.ds.array.ContinuousMemory;

import java.util.List;

public class Util {

    public static void main(String[] args) {
	// write your code here
        List<Integer> result = ContinuousMemory.getSubArraySum(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},15);

        for(int x: result){
            System.out.println(x);
        }
    }
}
