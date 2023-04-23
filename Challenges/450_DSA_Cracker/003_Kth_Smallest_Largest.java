
import java.util.ArrayList;
import java.util.Collections;

public class Solution {
	public static ArrayList<Integer> kthSmallLarge(ArrayList<Integer> arr, int n, int k) {
		Collections.sort(arr);
		ArrayList<Integer> res = new ArrayList<>();
		res.add(arr.get(k-1));		
		res.add(arr.get(n-k));
		return res;
	}
}
