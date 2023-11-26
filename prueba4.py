import requests
import base64
from io import BytesIO

id = 4
url = "https://api-healtcare-ultima.onrender.com/appointment/{}".format(id)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")


'''
if response.status_code == 200:
    
    data = response.json()
    if "pdf_data" in data:
        
        pdf_bytes = base64.b64decode(data["pdf_data"])
        
       
        with open("citas_medicas.pdf", "wb") as pdf_file:
            pdf_file.write(pdf_bytes)
        
        print("PDF descargado con éxito como citas_medicas.pdf")
    else:
        print("No se encontraron datos binarios en la respuesta JSON")
else:
    print(f"Error: {response.status_code} - {response.text}")
'''