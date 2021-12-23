def to_string(f):
    file = ""
    for j in f:
        file = file + str(j)
    x = []
    k = []
    ss = ""
    for j in file:
        if j == '<':
            k.append(ss.replace("\n", "").strip())
            ss = j
        elif j == ">":
            ss += j
            k.append(ss.replace("\n", "").strip())
            ss = ""
        else:
            ss += j

    for j in range(len(k)):
        if k[j] == "":
            continue
        x.append(k[j])
    return x


def openTag(tag):
    if tag[0] == "<" and tag[1] != "/" and tag[-1] == ">":
        return True
    return False


def closeTag(tag):
    if tag[0] == "<" and tag[1] == "/" and tag[-1] == ">":
        return True
    return False


def data(tag):
    if not openTag(tag) and not closeTag(tag):
        return True
    return False


def check(name):
    data = ""
    with open(name, "r") as myFile:
        data = myFile.readlines()
    st = to_string(data)
    stack = []
    for line in st:
        if openTag(line):
            stack.append(line)
        elif closeTag(line):
            if stack[-1] == line.replace("/", ""):
                stack.pop(-1)
            else:
                stack.append(line)
    if len(stack) == 0:
        return "balanced"
    else:
        return "not balanced"
