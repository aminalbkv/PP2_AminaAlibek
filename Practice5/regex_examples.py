import re

text = "Python is easy, Python is fun"

# re.search() - finds the first match
search_result = re.search(r"Python", text)
print("Search:", search_result.group())


# re.findall() - finds all matches
findall_result = re.findall(r"Python", text)
print("Findall:", findall_result)


# re.split() - splits the string
split_result = re.split(r"\s", text)
print("Split:", split_result)


# re.sub() - replaces text
sub_result = re.sub(r"Python", "Java", text)
print("Sub:", sub_result)