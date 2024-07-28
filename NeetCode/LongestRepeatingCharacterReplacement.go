/*
We hve to make cconsider a window.
Now, this window can be converted to a wondow with all repeating characters by changing at most k characters.

So, if window length - maxFrequency <= k, we can change the characters to get a window with all repeating characters.

We keep increasing the right pointer and updating the counters.
Once we reach a point where the window length - maxFrequency > k, we start moving the left pointer.

#### Why does maxF make sense?

We know that answer can only be updated when the window length - maxFrequency <= k.
Now if we ever go for a higher window length, that means the maxFrequency has to increase as well.
In all other cases where maxFrequency decreases, the window length will also decrease. To maintain the <= k condition.
*/
package main

func characterReplacement(s string, k int) int {
	l := len(s)

	if k >= l {
		return l
	}

	var left, right, ans, maxF = 0, 0, 0, 0
	m := make(map[byte]int)

	for {
		// while right pointer is less than length of string
		if right == l {
			break
		}

		// if window is valid, increase the right pointer
		if (right-left)-maxF <= k {
			// increment counter
			m[s[right]]++

			// update maxF
			if m[s[right]] > maxF {
				maxF = m[s[right]]
			}

			// update the pointer
			right++

			// 1. Check if the condition is still valid after the update
			// 2. Check if the window length is greater than the answer
			// If both conditions are true, update the answer
			if (right-left)-maxF <= k && right-left > ans {
				ans = right - left
			}
		} else {
			// if window is not valid, move the left pointer
			m[s[left]]--
			left++
		}
	}

	return ans
}
