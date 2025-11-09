text = input()
text = text.lower()
vowels = "aeiou"
count  = 0

for i in text:
    if i in vowels:
        count += 1

print(count)
