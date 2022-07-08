import requests
res = requests.get('https://www.gutenberg.org/cache/epub/68463/pg68463.txt')
txt = (res.text)
txt_to_list = txt.split()
count = {}
dup_count = {}
for i in txt_to_list:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
        dup_count[i] = count[i]
new_dup_count = sorted(
    dup_count.items(), key=lambda item: item[1], reverse=True)
print(
    f"The most used word is \'{new_dup_count[0][0]}\' and it is used for \'{new_dup_count[0][1]}\' times")
