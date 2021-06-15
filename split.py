def validateCommaSeperatedNumbers(inp):
    arr = inp.split(",")

    try:
        arr = [int(i) for i in arr]
        return arr
    except:
        return "Send only data in numbers format"
