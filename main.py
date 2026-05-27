# main.py
from funciones import calcular_promedio

def registrar_aprendiz():
    print("--- Registro de Aprendiz SENA ---")
    nombre = input("Ingrese el nombre del aprendiz: ")
    
    # Captura de notas
    nota1 = float(input("Ingrese la nota 1 (0.0 - 5.0): "))
    nota2 = float(input("Ingrese la nota 2 (0.0 - 5.0): "))
    nota3 = float(input("Ingrese la nota 3 (0.0 - 5.0): "))
    
    # Cálculo mediante el módulo importado
    promedio_final = calcular_promedio(nota1, nota2, nota3)
    
    print("\n--- Resultado del Registro ---")
    print(f"Aprendiz: {nombre}")
    print(f"Promedio Final: {promedio_final:.2f}")
    
    if promedio_final >= 3.5:
        print("Estado: Aprobado")
    else:
        print("Estado: No aprobado")

if __name__ == "__main__":
    registrar_aprendiz()