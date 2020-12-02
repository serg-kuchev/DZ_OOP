def readfile(name):
    import json
    with open(name, encoding='utf-8') as f:
        json_data = json.load(f)
        text = ''
        for items in json_data['rss']['channel']['items']:
            text += ' ' + items['description']
    return text


def count(n, text):
    new_list = text.split(' ')
    word_value = {}
    for word in new_list:
        if len(word) > n:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value


def sort(ccount, word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top = {}
    for word in sort_list:
        top[count] = word
        count += 1
        if count == ccount+1:
            break
    return top


def main():
    top_10 = third
    for i in top_10.values():
        print(i[1], ': ', i[0])


first = readfile('newsafr.json')
second = count(6, first)
third = sort(10, second)
main()


