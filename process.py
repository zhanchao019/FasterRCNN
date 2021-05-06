file = open("2007_train.txt")
write_file = open('./new.txt','a+')
for line in file:
  tmp=line[43:]
  write_file.writelines(tmp)
file.close()
write_file.close()