
public class Solution {
	public static String calculateFactorial(int n) {
        
        int zeros = 0, LEN = 1200, md, balance = 0, prod, rind;
        int[] ans = new int[LEN];
        ans[LEN-1] = 1;
        rind = LEN-1;
        
        for(int i=1; i<=n; i++) {
            md = i;
            while(md%10 == 0 && md != 0) {
                zeros += 1;
                md /= 10;
            }

            for(int j=LEN-1; j>=0; j--) {
                prod = ans[j] * md + balance;
                ans[j] = prod%10;
                balance = prod/10;
                if(j<rind && balance == 0 && ans[j]==0) {
                    rind = j;
                    break;
                }
            }
        }

        String s = "";
        int ind = 0;
        for(int i=0; i<LEN; i++) {
            if(ans[i] != 0) {
                ind = i;
                break;
            }
        }

        for(int i=ind; i<LEN; i++) {
            s += String.valueOf(ans[i]);
        }
        for(int i=0; i<zeros; i++) {
            s += "0";
        }
        return s;
	}
}
