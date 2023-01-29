def sort_by(mode= 1):
    temp = []
    with open('phone_book.csv', 'r') as file:
        for str in file:
            temp.append(str.split(';'))
    temp = sorted(temp, key=lambda x: int(x[mode]) if mode == 0 else x[mode])

    for str in temp:
        result = ''
        for i in range(len(str) - 1):
            result += str[i] + ';'
        else: result += str[len(str) - 1]
        with open('sorted_book.csv', 'a') as file:
            file.write(result)