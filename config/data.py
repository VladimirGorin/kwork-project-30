
filesArr = [
    "./settings/" + "sendMessageInDirectText.txt",
    "./settings/" + "ParseGroupUsersNick.txt",
    "./settings/" + "ParseGroupUsersCounter.txt"
]

text = []

with open(filesArr[0], "r", encoding="utf8", errors="ignore") as file:
    # chat info
    chatTextInfo = file.readlines()
    i = 0
    while i < chatTextInfo.__len__():
        text.append(chatTextInfo[i])

        i = i + 1

with open(filesArr[1], "r") as file:
    # parse sub
    groupParseSub = file.readline()


with open(filesArr[2], "r") as file:
    # parse counter
    groupParseCt = file.readline()


username = "nuhaaa0q"
password = "asd12345"

users_settings_dict = {
    'user1': {
        'login': 'nuhaaa0q',
        'password': 'asd12345',
        'users': ['lebedz.kris', "nonname", "lebedz.kris"]
    },
    'user2': {
        'login': 'nuhaaa0q',
        'password': 'asd12345',
        'users': ['nonname', 'marin']
    }
}

# Текст который мы отправляем

updt = f""

i = 0
while i < text.__len__():

    updt += text[i]

    i = i + 1


sendText = updt
print(sendText)


# Пользователь у которого нужно спарсить аудиторию
user_search = groupParseSub
user_sub_counter = int(groupParseCt)


# Сколько аккаунтов нужно создать
account_counter = 3  # указывайте на ондо число больше не 5 - а 6
