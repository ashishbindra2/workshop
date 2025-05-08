# Coding Question

## Given a string `s = "abcvderndsgh"` and an integer `k = 2`, divide the string into segments of length `k`, and **reverse every alternate 2 segments**, starting with skipping the first 2 segments.

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