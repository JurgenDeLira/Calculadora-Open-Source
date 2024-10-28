import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("0. Salir")

def pedir_numeros(cantidad=2):
    numeros = []
    for i in range(cantidad):
        numero = float(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)
    return numeros

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a, b = pedir_numeros()
            print(f"Resultado: {sumar.sumar(a, b)}")
        
        elif opcion == "2":
            a, b = pedir_numeros()
            print(f"Resultado: {resta.restar(a, b)}")
        
        elif opcion == "3":
            a, b = pedir_numeros()
            print(f"Resultado: {multiplicacion.multiplicar(a, b)}")
        
        elif opcion == "4":
            a, b = pedir_numeros()
            try:
                print(f"Resultado: {dividir.dividir(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "5":
            n = int(input("¿Cuántos números quieres sumar? "))
            numeros = pedir_numeros(n)
            print(f"Resultado: {suma_avanzada.suma_avanzada(numeros)}")
        
        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
