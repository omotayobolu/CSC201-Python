EnglishYoruba = {}

max_length = 6

while len(EnglishYoruba) < max_length:
    english = input("Enter english word: ")
    yoruba = input("Enter yoruba word: ")

    EnglishYoruba[english] = yoruba

    print(EnglishYoruba)    
    print(sorted(EnglishYoruba.items(), key=lambda x:x[1]))