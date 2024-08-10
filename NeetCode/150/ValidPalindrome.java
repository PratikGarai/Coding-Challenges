/*
 * Two pointers, left and right.
 * Comapre ignorecase for valid alphanumeric.
 */
class Solution {
    public boolean isPalindrome(String s) {
        int l=0, r=s.length()-1;
        char cl, cr;
        while(l<r) {
            cl = s.charAt(l);
            if(!(Character.isDigit(cl) || Character.isAlphabetic(cl))) {
                l++;
                continue;
            }
            cr = s.charAt(r);
            if(!(Character.isDigit(cr) || Character.isAlphabetic(cr))) {
                r--;
                continue;
            }

            if(Character.toLowerCase(cl) != Character.toLowerCase(cr)) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
}