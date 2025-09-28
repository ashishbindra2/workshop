# Coding Question

```py
str = "I \nlove \tGeeksforGeeks"
print(repr(str))
'I \nlove \tGeeksforGeeks
```

## Given a string `s = "abcvderndsgh"` and an integer `k = 2`, divide the string into segments of length `k`, and **reverse every alternate 2 segments**, starting with skipping the first 2 segments

Let’s break it down:

1. Divide the string into groups of `k` characters:

   * With `k = 2`, `s = ["ab", "cv", "de", "rn", "ds", "gh"]`

2. Reverse every alternate *pair* of segments, **starting after the first pair**:

   * Skip the first two: `["ab", "cv"]`
   * Reverse the next two: `["rn", "de"] → ["de", "rn"]`
   * Skip or stop (if fewer than 2 remain), last two: `["ds", "gh"] → not reversed`

3. Final sequence: `["ab", "cv", "de", "rn", "ds", "gh"]`

Join them back: `"abcvdern dsgh"`

But this would only make sense if your rule is to *reverse every two "words" or chunks of size k after skipping the first two*.

```py
s = "abcdefghij"
k = 2

l = True
d = ''
for i in range(0,len(s),k):
    if l:
        d = d + ''.join(reversed(s[i:i+k]))
        l=False
    else:
        d = d+ s[i:i+k]
        l = True

print(d)
```

```py
s = "abcdefghij"
k = 2

words = []

for i in range(0, len(s), k):
    # Reverse the chunk if it's at an even index, otherwise keep it as is
    chunk = s[i:i+k]
    words.append(''.join(reversed(chunk)) if (i // k) % 2 == 0 else chunk)

print(words)
```

Strings are called Identical if they contain the same characters.

 For example, "good" and "god" are similar since both consist of characters 'g', 'o', and 'd'.
 However, ''python'' and 'yarn'' are not similar since they do not contain similar characters.

 Find the number of sets (x,y) such that 0 str.length - 1 and the two strings strs[i] and strs[j] are identical.

  Example 1: Input: strs = ["good","god","yarn","bac","aabc"] 。
  Output: 2 Explanation: There are 2 pairs that satisfy the conditions: x=0 and y=1 :
  both strs |0| and strs[1] only consist of characters ' g ','o' and 'd'.
   x=3 and y=4 : both strs[3] and strs[4] only consist of characters ' a ', ' b ', and ' c '.

Example 2: Input: words = [''cba","nba","dba"] Output: 0 Explanation: Since there does not exist any pair that satisfies the conditions, we return 0. Constraints: 1 .length 1 [i].length strs[i] consist of only lowercase English letters.
