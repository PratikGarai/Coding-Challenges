/*
	Here, we know that window size of substring in s2 will have to be of the same size as s1.
	So, we can have an initial window of len(s1) and then keep on moving the window to the right.

	While moving, we can keep count of characters in the window and compare the same to character counts in s2.

	Now there are 2 ways to verify the window:
		1. Keep a map of character counts in window and compare all 26 characters after every move.
		2. a. Keep a map of character counts in s1.
		   b. Keep a map of character counts in window.
		   c. Keep a count of characters that match in both maps.
		   d. If count of characters that match is 26, then we have a match.
		   e. With each move, update the count of characters that match.
		   f. Now, we can check for updates in the match directly. We look for the follwing 4 conditions:
		   		- If left pointer was correct earlier, but does not match now. Reduce the match count.
		   		- If left pointer matches now. Increase the match count.
		   		- If right pointer was correct earlier. Reduce the match count.
		   		- If right pointer matches now. Increase the match count.

		Another possible optimization is to ignore the conditional checks if the character to be removed and added are the same.
*/

package main

func checkInclusion(s1 string, s2 string) bool {
	var l1, l2 = len(s1), len(s2)

	if l2 < l1 {
		return false
	}

	m1 := make(map[int]int)
	m2 := make(map[int]int)

	for i := 0; i < l1; i++ {
		m1[int(s1[i])]++
	}

	var l, r, matches = 0, l1 - 1, 0
	for i := 0; i < l1; i++ {
		m2[int(s2[i])]++
	}

	// inital window count
	for i := int('a'); i <= int('z'); i++ {
		if m1[i] == m2[i] {
			matches++
		}
	}

	// initial window check
	if matches == 26 {
		return true
	}

	for {
		if r >= l2-1 {
			break
		}

		// If the character to be removed and added are the same, then no need to update the maps
		if s2[l] == s2[r+1] {
			l++
			r++
			continue
		}

		m2[int(s2[l])]--
		m2[int(s2[r+1])]++

		// If left pointer was correct earlier, but does not match now
		if m2[int(s2[l])]+1 == m1[int(s2[l])] && m2[int(s2[l])] != m1[int(s2[l])] {
			matches--
		}
		// If left pointer matches now
		if m2[int(s2[l])] == m1[int(s2[l])] {
			matches++
		}

		// If right pointer was correct earlier
		if m2[int(s2[r+1])]-1 == m1[int(s2[r+1])] && m2[int(s2[r+1])] != m1[int(s2[r+1])] {
			matches--
		}
		// If right pointer matches now
		if m2[int(s2[r+1])] == m1[int(s2[r+1])] {
			matches++
		}

		if matches == 26 {
			return true
		}

		l++
		r++
	}

	return false
}
