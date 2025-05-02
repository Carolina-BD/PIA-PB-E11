import requests

ID = ["CA", "MX", "US", "BR", "CL"]


def obtener_datos(año_inicio, año_final):
    for i in ID:
        url = f"http://api.worldbank.org/v2/country/{i}/indicator/NY.GDP.MKTP.CD?format=json&date={año_inicio}:{año_final}&per_page=1000"
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()

            paises = {
                "CA": "Canadá",
                "MX": "México",
                "US": "Estados Unidos",
                "BR": "Brazil",
                "CL":"Chile"
                }
            print(f"\nPIB de {paises[i]}: ")

            
            for dato in datos[1]:
                print(f"{dato['date']}: {dato['value']}")
        except requests.exceptions.ConnectionError:
            print("Error de conexión. Revise su conexión a internet.")
        except requests.exceptions.Timeout:
            print("La solicitud tardó demasiado en responder.")
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP: {e}")
    
    

while True:
    try:
        año_inicio = int(input("Ingrese el año inicial (entre 1960 y 2023): "))
        año_final = int(input("Ingrese el año final (entre 1960 y 2023): "))
        if año_inicio < 1960 or año_final > 2023 or año_inicio > año_final:
            raise ValueError("Rango inválido")
        break
    except ValueError as e:
        print(f"Error en la entrada: {e}. Inténtalo de nuevo.")


obtener_datos(año_inicio, año_final)
