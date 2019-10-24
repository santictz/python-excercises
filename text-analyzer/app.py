#Simple Python script to analyze text
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count +1
    return count


filename = input('Enter a filename: ')

with open(filename) as f:
    text = f.read()

print(f"There are {count_char(text, 't')} t characters in the text")

#finds what percentage of the text each character of the alphabet occupies.
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print(f"{char} - {round(perc, 2)}%")