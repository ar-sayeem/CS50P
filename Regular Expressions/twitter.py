### - - - Extract user name from twitter profile link - - - ###

import re

url = input("URL: ").strip()

if matches := re.search(r"https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



# username = re.sub(r"^(http?s://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# http?s == http or https

# re.sub(pattern, repl, string, count=0, flags=0)
# substitute with "" means nothing