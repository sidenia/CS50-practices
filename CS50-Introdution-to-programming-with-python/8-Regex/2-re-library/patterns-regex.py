de Regex, re search pattern symbols:

.       any character except newline
*       0 or more repetitions
+       1 or more repetitions
?       0 or 1 repetitions
{m}     exactly m repetitions
{m,n}   m to n repetitions
^       matches the start of string
$       matches end of string or just before the newline at the end of string
[]      set of characters
[^]     complementing the set (you cannot match any of the characters)
    ex: [^@] accept everything except @

######## CHARACTER CLASSES ########

\d      (any digit) decimal digit
\D      (any non-digit) not a decimal digit
\s      (any whitespace) whitespace
\S      (any non-whitespace) not a whitespace
\w      (any alphanumeric) character, number and _
\W      (any non-alphanumeric) not a word character

A|B     condition to be used in a list, parameters are necessary for:
(...) group
(?...) non-capturing group