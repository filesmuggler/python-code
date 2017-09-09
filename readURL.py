from six.moves.urllib.request import urlopen
import re



link = input("Enter link to search: ")
response = urlopen(link)
content = response.read()
print(content)

s_content = str(content)

s_found = "google found at "

file = open('result-webpage.txt','w')

for m in re.finditer('Mikrobot',s_content):
    print('Mikrobot found',m.start(),m.end())
    s_write = s_found + str(m.start()) +" "+ str(m.end())+ "\n"
    file.write(s_write)


file.close()