def readfile(name):
    import json
    with open(name, encoding='utf-8') as f:
        json_data = json.load(f)
        text = ''
        for items in json_data['rss']['channel']['items']:
            text += ' ' + items['description']
    return text


def count(text):
    n = int(input('Введите количество буквы:'))
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
    ccount = int(input('Введите количество слов ')) + 1
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
    name = input('Введите имя файла: ')
    top_10 = sort(count(readfile(name)))
    for i in top_10.values():
        print(i[1], ': ', i[0])


main()
