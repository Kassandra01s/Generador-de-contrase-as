import random
import string
def solicitar_longitud():
    while True:
        try:
            longitud = int(input("Ingresar la longitud de la contraseña (entre 8 y 12 caracteres): "))
            if 8 <= longitud <= 12:
                return longitud
            else:
                print("La contraseña debe tener al menos 8 caracteres y máximo 12 caracteres.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def seleccionar_caracteres():
    print("Seleccione el tipo de caracteres a incluir en la contraseña:")
    mayusculas = input("¿Incluir mayúsculas? (A-Z)? (S/N): ").lower() == 's'
    minusculas = input("¿Incluir minúsculas? (a-z)? (S/N): ").lower() == 's'
    numeros = input("¿Incluir números? (0-9)? (S/N): ").lower() == 's'
    simbolos = input("¿Incluir símbolos? (@#$%*)? (S/N): ").lower() == 's'
    
    if not any([mayusculas, minusculas, numeros, simbolos]):
        print("Debe seleccionar al menos un tipo de carácter.")
        return seleccionar_caracteres()
    return mayusculas, minusculas, numeros, simbolos

def generar_contraseña(longitud, caracteres):
    mayusculas, minusculas, numeros, simbolos = caracteres
    conjunto_caracteres = ''
    
    if mayusculas:
        conjunto_caracteres += string.ascii_uppercase
    if minusculas:
        conjunto_caracteres += string.ascii_lowercase
    if numeros:
        conjunto_caracteres += string.digits
    if simbolos:
        conjunto_caracteres += '@#$%*'
    
    if not conjunto_caracteres:
        raise ValueError("No se seleccionaron caracteres para la contraseña.")

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(conjunto_caracteres) for _ in range(longitud))
    
    if validar_contraseña(contraseña, caracteres):
        return contraseña
    else:
        # Si la contraseña no cumple, generar otra
        return generar_contraseña(longitud, caracteres)

def validar_contraseña(contraseña, caracteres):
    mayusculas, minusculas, numeros, simbolos = caracteres
    if mayusculas and not any(c.isupper() for c in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    if minusculas and not any(c.islower() for c in contraseña):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False
    if numeros and not any(c.isdigit() for c in contraseña):
        print("La contraseña debe contener al menos un número.")
        return False
    if simbolos and not any(c in '@#$%*' for c in contraseña):
        print("La contraseña debe contener al menos un símbolo (@#$%*).")
        return False
    return True
# Programa principal
def main():
    longitud = solicitar_longitud()
    caracteres = seleccionar_caracteres()
    contraseña = generar_contraseña(longitud, caracteres)
    print("Contraseña generada:", contraseña)

if __name__ == "__main__":
    main()
    
