def readfile(name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(name, parser)
    root = tree.getroot()
    news_xml = root.findall("channel/item")
    for news in news_xml:
        text = news.find('description')
        return text.text


def count(text):
    new_list = text.split(' ')
    word_value = {}
    for word in new_list:
        if len(word) > n:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value


def sort(word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top = {}
    for word in sort_list:
        top[count] = word
        count += 1
        if count == ccount:
            break
    return top


def main():
    top_10 = sort(count(readfile(name)))
    for i in top_10.values():
        print(i[1], ': ', i[0])


name = input('Введите имя файла: ')
ccount = int(input('Введите количество слов ')) + 1
n = int(input('Введите количество букв: '))

main()
