/*
    Similar to Permutation In String, we have to keep a sliding window in the bigger string and check if it is a vaild one or not.

	There are two maps, one for the bigger string and one for the smaller string. We keep track of the count of characters in both the maps.

	Here is what we do :
		1. Create the first substring of the bigger string. It is of the same length as the smaller string.
		2. We keep ```matches``` and ```dchars``` to keep track of the number of characters that match in the substring and the smaller string.
			- ``matches`` is the number of characters that match in the substring and the smaller string.
			- ``dchars`` is the number of distinct characters in the smaller string.
			- If ```matches``` == ```dchars```, we have a valid substring.
		3. Now, in the loop :
			- If the substring is valid, we check if it is the minimum substring.
				- We update the global answer.
				- We move the left pointer to the right.
				- If the character at the left pointer is important, we check if it was correct earlier and is not correct now.
			- If the string is not valid, we move the right pointer to the right.
				- If the character at the right pointer is important, we check if it was not correct earlier and is correct now.
		4. If the condition is never satisfied, we return an empty string.
		5. Else, we return the substring.

	A difference in the check condition is that now we have partial checks after each update.
	This is because the string can now contain more characters than the smaller string.
	Since the equality conditions have now been relaxed, we have lesser conditions to check.
*/

package main

func minWindow(s string, t string) string {
	var l1, l2 = len(s), len(t)

	if l2 > l1 {
		return ""
	}

	// count in larger/target string
	m1 := make(map[byte]int)
	// count in smaller/truth string
	m2 := make(map[byte]int)

	for i := 0; i < l2; i++ {
		m2[t[i]]++
	}

	// left, right
	var l, r = 0, 0
	// global minimum span
	var ml, mr = -1, l1
	// disticnt chars in sources, matches in current span
	var dchars, matches = 0, 0

	// update count in the first substring
	for r = 0; r < l2; r++ {
		m1[s[r]]++
	}

	// First substring is answer
	for k, _ := range m2 {
		dchars++
		if m2[k] <= m1[k] {
			matches++
		}
	}

	if dchars == matches {
		return s[0:l2]
	}

	for {
		// If current substring is a match
		if dchars == matches {
			// Check if it minimum
			if (r - l) < (mr - ml) {
				mr = r
				ml = l
			}

			// Update left
			m1[s[l]]--
			l++

			// If the character matters
			if m2[s[l-1]] != 0 {
				// If left was correct earlier, but got reduced now
				if m1[s[l-1]] < m2[s[l-1]] {
					matches--
				}
			}
		} else {
			// Check if right expansion is possible
			if r >= l1 {
				break
			}

			// Expand right
			m1[s[r]]++
			r++

			// If the character matters
			if m2[s[r-1]] != 0 {
				// If right was not correct earlier, but got in range now
				if m1[s[r-1]] == m2[s[r-1]] {
					matches++
				}
			}
		}
	}

	// if condition never satisfied
	if ml == -1 {
		return ""
	}

	return s[ml:mr]
}
