from string import ascii_lowercase
from getpass import getpass

password = getpass('Ingresa tu contraseña: ').lower()
count = 0
for letra in password:
    for letra2 in ascii_lowercase:
        count += 1
        if letra == letra2:
            break
        
print(f'La contraseña fue forzada en {count} intentos')
           