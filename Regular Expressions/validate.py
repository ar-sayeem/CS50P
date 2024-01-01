# re library
# docs.python.org/3/library/re.html
# re.search(pattern, string, flags=0)
# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags)



import re

email = input("What's your email? ").strip()        # .lower()

if re.search(r"^(\w|\.|)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):         # (r"^[^@]+@[^@]+\.edu\.bd$", email)
    print("Email is valid")
else:
    print("Email is invalid")


#   r           indicates a raw string which will not interprate a '\'
#   \.          means i don't want any character, just want literally a dot there before edu
    

### - - - Expressions - - - ###
#   something then @ then something     #

#   .           any character except a newline
#   *           0 or more repetitions
#       .* == +
#   +           1 or more repetitions
#   ?           0 or 1 repetition
#   {m}         m repetitions
#   {m, n}      m-n repetitions

#   ^           matches the start of the string
#   $           matches the end of the string or just
#               before the newline at the end of the string

#   []          set of characters   [a-zA-Z0-9_]
#   [^]         complementing the set
#   [^@]        any character except @


### - - - instead of [] we can directly use - - - ###

#   \d          decimal digit           [0-9]
#   \D          not a decimal digit
#   \s          whitespace characters   [tab/space] / [a-zA-Z0-9_ ]
#   \S          not a whitespace character
#   \w          word character ... as well as letters, numbers and the underscore but not dot
#   \W          not a word character


### - - - OR - - - ###

#   A|B         either A or B
#   (...)       a group
#   (?:...)     non-capturing versions


### - - - re built in variables|constant - - - ###

#   re.IGNORECASE
#   re.MULTILINE
#   re.DOTALL


### - - - websites use - - - ###

#   ^[a-zA-Z0-9.!#$%&'*+\/=?^_`
#   {|}~-]+@[a-zA-Z0-9](?:[a-zA
#   -Z0-9-]{@,61}[a-zA-Z0-9])?(
#   ?:\.[a-zA-Z0-9](?:[a-zA-Z0-
#   9-]{0,61}[a-zA-Z0-9])?)*$