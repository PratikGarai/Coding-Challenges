/*
	Keep a counter hashmap for alphabet counter.

	Let the substring start from left = 0 to right = 0

	Now, we increase the right while updating count of the characters.
	Once we reach a point where the count of a charater goes above 1, we take a pause.
		Here, we start moving the left till the repeated character is ommited.
		We update the counters as we keep moving the left.
*/

package main

func lengthOfLongestSubstring(s string) int {
	// Counter hashmap
	m := make(map[byte]int)
	var gc, left, right int
	l := len(s)

	// If empty string
	if l == 0 {
		return 0
	}

	for {

		// Update counter of right
		m[s[right]] += 1

		// If count of character is more than 1
		if m[s[right]] > 1 {

			// Keep pushing left till the repeating character is ommited from the other side
			for {
				m[s[left]] -= 1
				left++
				if m[s[right]] == 1 {
					break
				}
			}
		}

		// Move the rihgt pointer
		right += 1

		// Update the result
		if (right - left) > gc {
			gc = right - left
		}

		if right == l {
			break
		}
	}

	// Update the result once more after the end of the array
	if (right - left) > gc {
		gc = right - left
	}

	return gc
}
