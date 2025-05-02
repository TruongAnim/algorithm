from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)
print(len(web2lowerset))

result = []
for i in web2lowerset:
    if len(i) == 8 and i[-2] == 'a' and i.count('a') == 1 and len(set(i)) == len(i):
        result.append(i)

print(len(result))
print(result)