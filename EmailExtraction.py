import re


def part2_regex():
    file = open("sample.txt", "rt")
    fileContents = file.read()
    output = re.findall(r"@softwire.com", fileContents)
    print(len(output))
    file.close()


def part3_dict():
    dict = {}
    file = open("sample.txt")
    fileContents = file.read()
    output = re.findall(r"(?<=@)[\w-]+(?=.)", fileContents)
    for item in output:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 0
    for key, value in dict.items():
        print(key, value)

    file.close()


def mostCommon10():
    dict = {}
    file = open("sample.txt")
    fileContents = file.read()
    output = re.findall(r"(?<=@)[\w-]+(?=.)", fileContents)
    for item in output:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 0

    sortedDict = {key: value for key, value in sorted(dict.items(), reverse=True, key=lambda item: item[1])}

    for i, (key, value) in enumerate(sortedDict.items()):
        if i == 10:
            break
        print(key, value)

    file.close()


def userDefinedFrequency():
    freq = int(input("Please enter a number: "))
    dict = {}
    file = open("sample.txt")
    fileContents = file.read()
    output = re.findall(r"(?<=@)[\w-]+(?=.)", fileContents)
    for item in output:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 0

    sortedDict = {key: value for key, value in sorted(dict.items(), reverse=True, key=lambda item: item[1])}

    for key, value in sortedDict.items():
        if dict[key] >= freq:
            print(key, value)

    file.close()


part2_regex()
# part3_dict()
# mostCommon10()
# userDefinedFrequency()
