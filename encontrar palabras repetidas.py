import io

text=open("pro encontrar palabras repetidas.txt","r")
text_read=text.read()
text.close()


text_read=text_read.lower()

signos="-:;.,/*-+\n!·$%&/()=?¿[]""''"

for caracter in signos:
    text_read=text_read.replace(caracter," ")

text_read=text_read.split()

dic={}

for palabra in text_read:
    if palabra in dic:
        dic[palabra]+=1
    else:
        dic[palabra]=1

resultados=open("resultados.txt","a")



for element in dic:
    num_rep=dic[element]
    resultados.write("La palabra: "+str(element)+"-- esta repetida: "+str(num_rep)+" --veces.\n")

print("reporte guardado con exito")
resultados.close()