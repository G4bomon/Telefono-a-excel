import pandas as pd
from whatsapp_api_client_python import API
import numpy as np

# Initialize the API witht the data

greenAPI = API.GreenAPI(
    "*************", # your Id instance
    "******************************************" # your apiTokenInstance
)
# Here you can chance the document path to your document and the sheet name
df = pd.read_excel('c:/Codigo cosas columnares/Circulo_de_Abuelos_General.xlsx', sheet_name='Sheet1')
# Here imput the row of the name and the phone 
nombres = df.iloc[:, [1]]
telefonos= df.iloc[:, [4]]



#convertions
nombres_array = nombres.values.flatten()  
telefonos_array = telefonos.values.flatten() 

# You can set the prefix to this, this code will add 58 to the firs part of the phone number

new_first_digit = '58' 

# Create a new array to hold the modified phone numbers
modified_telefonos_array = []

for numero in telefonos_array:
    # Convert the number to a string
    numero_str = str(numero)
    
    # Change the first digit
    modified_numero = new_first_digit + numero_str  # Keep the rest of the number

    # Append the modified number to the new array
    modified_telefonos_array.append(modified_numero)

# Convert the list back to a NumPy array if needed
modified_telefonos_array = np.array(modified_telefonos_array)


for index, persona in enumerate(nombres_array):
    numero = modified_telefonos_array[index]
    contact = {
    "phoneContact": numero, 
    "firstName": persona
    }
    response = greenAPI.sending.sendContact("58*************@c.us",contact) # Here put the numbers you want to put the contacts in
    print(response.data)
