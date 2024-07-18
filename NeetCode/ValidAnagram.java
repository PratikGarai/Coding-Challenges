/*
 * Check for length matching.
 * 
 * If alphabet in s1, increase the count.
 * If alphabet in s2, decrease the count.
 * 
 * If anagram, count should be same. So all characters new count should be 0.
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        short[] count = new short[26];

        if(s.length() != t.length())
        return false;

        for(int i=0; i<s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for(short j : count) {
            if(j != 0) {
                return false;
            }
        }

        return true;
    }
}