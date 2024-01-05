import re

def find_match(regex, string):
    compiled_regex = re.compile(regex)

    match = compiled_regex.search(string)

    if match is None:
        print("<NONE>")
    else:
        print(f"{match.start()}: {match.group()}")
        for i, group in enumerate(match.groups(), 1):
            if (group):
                print(f"{i}/{match.start(i)}: {group}")

        for name, group in match.groupdict().items():
            if (group):
                print(f"{name}/{match.start(name)}: {group}")

# Пример использования
regex = input()
while True:
    st = input()
    if not st:
        break
    find_match(regex, st)
