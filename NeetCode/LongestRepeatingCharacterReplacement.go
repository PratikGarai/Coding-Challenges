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
		if right == l {
			break
		}

		if (right-left)-maxF <= k {
			m[s[right]]++
			if m[s[right]] > maxF {
				maxF = m[s[right]]
			}

			if (right - left) > ans {
				ans = (right - left)
			}

			right++
		} else {
			m[s[left]]--
			left++
		}
	}

	if (right-left)-maxF <= k {
		if right-left > ans {
			ans = right - left
		}
	}

	return ans
}
