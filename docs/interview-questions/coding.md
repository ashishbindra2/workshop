# Coding Question

### 721. Accounts Merge (asked in amazon ) Medium

Problem link: <https://leetcode.com/problems/accounts-merge/editorial/>
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

```yaml
Input: accounts = [
["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]
]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


Explanation:
The first and second John's are the same person as they have the common email "<johnsmith@mail.com>".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
```

```py
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = [acc[0] for acc in accounts]
        new = [set(acc[1:]) for acc in accounts]

        merged = True
        while merged:
            merged = False
            i = 0

            while i < len(new):
                j = i + 1
                while j < len(new):
                    if new[i] & new[j]:
                        new[i] |= new[j]
                        del new[j]
                        del names[j]
                        merged = True

                    else:
                        j += 1
                i += 1

        for i, name in enumerate(names):
            new[i] = [name] + sorted(new[i])
        return new
```

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
