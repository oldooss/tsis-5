import re

#1

def textMatch(text):
    patt = '^a(b*)$'
    if re.search(patt, text):
        return "Found match!"
    else:
        return "Not matched"


print(textMatch("ab"))
print(textMatch("ac"))


#2

def text_match(text):
    patt = 'ab{2,3}'
    if re.search(patt, text):
        return 'Found a match!'
    else:
        return 'Not matched!'


print(text_match("ab"))
print(text_match("aabbbbbc"))

#3

def text_match(text):
    patt = '^[a-z]+_[a-z]+$'
    if re.search(patt, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

#4

def text_match(text):
    patt = '[A-Z]+[a-z]+$'
    if re.search(patt, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("Aidos"))
print(text_match("aidos"))
print(text_match("AIDOS"))
print(text_match("aA"))
print(text_match("Aa"))

#5

def text_match(text):
    patt = 'a.*?b$'
    if re.search(patt, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

#6

text = 'Kazakh British, Technical University.'
print(re.sub("[ ,.]", ":", text))

#7

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('Arthur_Morgan'))

#8

text = "KazakhBritishTechnicalUniversity"
print(re.findall('[A-Z][^A-Z]*', text))

#9

def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("kbtu"))
print(capital_words_spaces("KazakhBritishTechnicalUniversity"))
print(capital_words_spaces("KazakhBritishTechnicalUniversity"))

#10

def camel_to_snake(text):
    string1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string1).lower()


print(camel_to_snake('KazakhBritishTechnicalUniversity'))
