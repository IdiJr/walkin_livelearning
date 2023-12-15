#character classes
They define a set of characters to match.
Examples:
* `/[a-z]/` - matches any lowercase letter
* `/[A-Z]/` - matches any uppercase letter
* `/[0-9A-F]/` - matches any character from 0-9 and uppercase letters from A-F
* `/[^a-zA-Z0-9]/` - matches any character that is not in the ranges specified

# Quantifiers
* `.` - matches any character except a newline (two matches 2 characters and so on)
* `+`- matches one or more occurance of a character
* `\d` - matches any digits occurring
* `\D` - matches any character (same as [0-9])
* `\S` - matches any whitespace character
* `/[a+]/` - matches one or more of the character `a`
* `/[a*]/` - matches zero or more of the character `a`
* `/[a?]/` - matches zero or one of the character `a`
* `/a{2,4}/` - matches 2 - 4 occurrances of the character `a`

#Anchors
* `^` - matches strings that starts with the specified string
* `$` - matches ends that starts with the specified string
eg: `/^alx[0-9]{2}hello[A-Z]$/` - matches 

# Grouping and capturing 
* `/ab/` - 
# Task ( example of practical use of regex)
Create password validator: 
`[a-z]{10, }` - takes lowercase characters that are 10 or more ([a-z]{10} - must have only 10)
`^[a-z]{6,}\d`

Email regex syntax:
`^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{3, })$` - matches any string starting with lowercase, uppercase, number, underscore, hyphen or period occurring once or more followed by `@` then, matches any string starting with lowercase, uppercase, number, underscore, hyphen or period occurring once or more followed by `.` then matches any string starting with lowercase, uppercase from three or more characters.
