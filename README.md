# Pattern-matching-using-design-patterns


- We use a Chain-of-Responsibility like solution to find substrings in a string with wild
characters. 
- The wild characters used are “*” and “.”
- The character “.” matches any single character. The character “*” matches zero or more characters. So “c.t” with match
“cat”, “cbt”, etc. While “c*t” with match “ct”, “cat”, “caat”, “cbt”, “casdert” and many others.
- Now a Match object will find the first match of a pattern in a string. For example in:

```
match = new Match( “c.t” );
startIndex = match.findFirstIn( “cacacat”);
```

- The goal is to implement the Chain-of-Responsibility, so regular expressions or other built-in pattern matchers are not used. The chain of objects are used to do the matching.
- There will be one object in the chain for each character in the pattern.
- Eg: If we use “ca.t” to illustrate. The chain for this pattern will contain at least four objects. 
	- The first object (head) in the chain needs to find the first occurrence of the character c in the target string and pass the target string and the location in the string to the next object in chain. 
	- If the next object in the chain reports success, then the head of the chain returns the location of the pattern. 
	- If the next object reports failure to match, the head object needs to find the second occurrence of c in the string. 
	- The head object will try all occurrences of c in the string until a match is found or it is determined that the pattern is not in the string.
	- The second object in the chain behaves slightly differently. It is given a position and the string from the head object. 
	- If the next character is an “a” it passes the request to match to the next object in the chain. It then reports to the head object the result returned by the rest of the chain. 
	- If the next character is not an “a” it returns failure to the head chain.

- Note the two following cases.

```
match = new Match( “c*t” );
assertEquals(0, match.findFirstIn( “cacacat”))
match = new Match( “c*tb” );
assertEquals(2, match.findFirstIn( “bacatatb”))
```