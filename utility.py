def getInputText(fileName):
    lines = []
    with open(fileName) as fp:
        contents = fp.read()
        lines = contents.split('\n')
    return lines