arquivo = open("/home/martini/dev/DataScienceLearning/python/file.txt", "r")
print(arquivo)
linhas = arquivo.readlines()
for i in linhas:
    print(i)
texto_completo = arquivo.read()
print(texto_completo)    

###
arquivo2 = open("/home/martini/dev/DataScienceLearning/python/fileW.txt","a")
arquivo2.write("Esse é o meu arquivo\n")
arquivo2.write("Coloquei mais uma linha\n")
arquivo2.close()
