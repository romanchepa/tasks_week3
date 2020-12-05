with open('referat.txt', 'r', encoding = 'utf-8')as referat_file:
  with open( 'referat2.txt', 'w') as new_referat_file:
    for line in referat_file:
      w = line.replace('.', '!')
      new_referat_file.write(w)
    referat_file.seek(0)
    content = referat_file.read()
    print(len(content))
    referat_file.seek(0)
    lines = referat_file.readlines()
    all_words = 0
    for index, value in enumerate(lines):
      words = len(value.split())        
      all_words += words 
    print(all_words)  
    

