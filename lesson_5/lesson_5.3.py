import string

my_str = input("Enter a string: ")
my_str = my_str.title()
my_str = my_str.translate(str.maketrans('', '', string.punctuation))
my_str = my_str.replace(" ", "")


hashtag = '#' + my_str
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)