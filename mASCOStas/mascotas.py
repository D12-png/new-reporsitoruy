import numpy as np
import json 
import os

def cargar_datos():
    try:
        with open('historial_mascotas.json', 'r') as file:
            data = json.load(file)
            mascotas =np.array(data)
    except FileNotFoundError:
        mascotas =np.empty((0,7), dtype=object)
        return mascotas
    #guardar archivos JSON de las mascotas

def guardar_datos(mascotas):
    with open('historial_pacientes.json', 'w') as file:
        json.dump(mascotas.tolist(), file)

def ingresar_ficha():
    nombre = input ("nombre de la mascota:")
    codigo = input ("codigo de la mascota:")
    edad = input ("edad de la mascota:")
    raza = input ("raza de la mascota:")
    peso = input("peso de la mascota:")
    diagnostico = input ("diagnostico de la mascota:")
    medicamentos = input("medicamentos de la mascota:")
    ficha = np.array([[nombre, codigo, edad, peso,raza,diagnostico, medicamentos]])
    return ficha  

def eliminar_ficha(codigo,Nombre):
    lista_actualizada_mascotas=[mascota for mascota in Nombre [1]!=codigo]
    return np.array(lista_actualizada_mascotas)

def buscar_ficha_por_codigo (mascotas,codigo):
    ficha_mascota = None
    for mascota in mascotas:
        if mascota[1]==codigo:
            ficha_mascota = mascotas
            break
    return ficha_mascota

def buscar_medicamentos_por_codigo(mascota, codigo):
    medicamentos_de_la_mascota = False
    for mascota in mascota:
        if mascota[1]==codigo: 
            print("El diagnostico de la consulta:{mascota[5]}")
            print("los medicamentos recetados para la mascota son:{mascota[6]}")
            medicamentos_de_la_mascota = True
    if not medicamentos_de_la_mascota:
                print("El paciente no tiene medicamentos preescritos")

def listar_mascotas(mascotas):
     for i, mascotas in enumerate(mascotas, start= 1):
          print("----------------------------------------------------")
          print(f"mascotas{i}:")
          print(f"nombre:{mascotas[0]}")
          print(f"Codigo:{mascotas[1]}")
          print(f"edad:{mascotas[2]}")
          print(f"peso:{mascotas[3]}")
          print(f"raza:{mascotas[4]}")
          print(f"diagnostico:{mascotas[5]}")
          print(f"medicamentos:{mascotas[6]}")
          print("----------------------------------------------------")


