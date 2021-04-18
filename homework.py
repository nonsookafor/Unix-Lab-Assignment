import sys


a = sys.argv[0]
b = sys.argv[1]
c = sys.argv[2]
c = c.upper()
st = ""
for i in c:
  num = ord(i)
  if 65 <= num <= 90: # to assure only letters from A toZ
    if num + int(b) <= 90:
      st += chr(num + int(b))
    else:
      st += chr((num + int(b) -26))
  else:
    pass


everything = ""
for i in range(len(st)):
  if i % 5 == 4:
    everything += st[i] + " "
  else:
    everything += st[i]
  if i % 50 == 49:
    everything += "\n"
    
print(everything)

# sample calling form in the terminal

#python3 homework.py 1 "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."