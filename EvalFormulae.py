import re
def evalform(form, *args):
    return eval(form, dict(zip(sorted(list(set(re.findall(r'[a-z]+', form)))), args)))