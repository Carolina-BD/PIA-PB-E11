from statistics import mean, stdev
import re

mex=[]
usa=[]
ca= []
cl=[]
br=[]

datos = {
"País": "Nombre",
"Año": 0,
"PIB" : 0
}


lista_paises =[]
regex_pib = re.compile(r'(\d+)|(\d+.\d+)')
regex_año = re.compile(r'20\d{2}')

contador=0

with open ("PIB_paises.csv", "r") as file:
    for row in file:
        contador += 1
        info = row.split(',')

        datos["País"]= info[0]
        datos["Año"]= info[1]
        datos["PIB"]= info [2]

        info[2]=info[2].replace('\n','')

        datos["PIB"]=info[2]

        if contador == 0:
            if regex_pib.match(str(info[2])):
                pass
            else:
                print("Dato invalido")

            if regex_año.match(str(info[1])):
                pass
            else:
                print("Dato invalido")

        copia_datos=datos.copy()

        if info[0]== "México":
            mex.append(copia_datos)

        if info[0]== "Estados Unidos":
            usa.append(copia_datos)

        if info[0]== "Canadá":
            ca.append(copia_datos)

        if info[0]=="Chile":
            cl.append(copia_datos)

        if info[0]=="Brasil":
            br.append(copia_datos)


        lista_paises.append(copia_datos)

mex_pib = []
for i in mex:
    mex_pib.append(float(i["PIB"]))
print(f"""
México 
PIB 2010-2020: {mex_pib}
Promedio: {mean(mex_pib)},
Desviación estándar: {stdev(mex_pib)}
""")

usa_pib = []
for i in usa:
    usa_pib.append(float(i["PIB"]))
print(f"""
Estados Unidos 
PIB 2010-2020: {usa_pib}
Promedio: {mean(usa_pib)},
Desviación estándar: {stdev(usa_pib)}
""")

cl_pib = []
for i in cl:
    cl_pib.append(float(i["PIB"]))
print(f"""
Chile 
PIB 2010-2020: {cl_pib}
Promedio: {mean(cl_pib)},
Desviación estándar: {stdev(cl_pib)}
""")
br_pib = []
for i in br:
    br_pib.append(float(i["PIB"]))
print(f"""
Brasil 
PIB 2010-2020: {br_pib}
Promedio: {mean(br_pib)},
Desviación estándar: {stdev(br_pib)}
""")
ca_pib = []
for i in ca:
    ca_pib.append(float(i["PIB"]))
print(f"""
Canadá 
PIB 2010-2020: {ca_pib}
Promedio: {mean(ca_pib)},
Desviación estándar: {stdev(ca_pib)}
""")

PIB_2010=[]
PIB_2020=[]

for i in lista_paises:
    if i["Año"] == "2010":
        PIB_2010.append(float(i["PIB"]))
    if i["Año"] == "2020":
        PIB_2020.append(float(i["PIB"]))

print(f"""
PIB Promedio y Desviación Estándar 
    2010
Promedio: {mean(PIB_2010)}
Desviación Estándar: {stdev(PIB_2010)}
    2020
PIB:{mean(PIB_2010)}
Desviación Estándar: {stdev(PIB_2020)}

""")

    

        

        
        
