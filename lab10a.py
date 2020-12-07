import re
mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
email = re.findall(r"\s\w+[._-]*\w+\@\w+\.*\w+\.\w+", mtxt)

#email = re.findall(r"(\s\w+(?:\.\w+)*@\w+\.\w+(?:\\w+)*)", mtxt)
print(email)