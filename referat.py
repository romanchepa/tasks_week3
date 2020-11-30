with open('referat.txt', 'r', encoding = 'utf-8')as f: # Читаем файл и считаем всю строку.
  content = f.read()
  print(len(content))


with open('referat.txt') as f: # Считаем количество слов в тексте
  lines = f.readlines()


with open('referat.txt', 'r') as f: # Считаем количество слов в тексте
    all_words = 0
    for index, value in enumerate(lines):
        words = len(value.split())        
        all_words += words
print(all_words)


referat_file = open('referat.txt', 'r') # Меняем точки в тексте на восклицательные знаки 
new_referat_file = open( 'referat2.txt', 'w')

for line in referat_file:
  w= line.replace('.', '!')
  new_referat_file.write(w)
referat_file.close()
new_referat_file.close()