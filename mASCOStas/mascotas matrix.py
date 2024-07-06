import numpy as np
from mascotas import cargar_datos, guardar_datos,ingresar_ficha, eliminar_ficha, buscar_ficha_por_codigo, buscar_medicamentos_por_codigo, listar_mascotas

listado_de_mascotas = cargar_datos()
listado_mascotas = listado_de_mascotas # Asignar el valor de listado_de_pacientes a listado_pacientes

while True:
    print("Menú:")
    print("1. Ingresar codigo de la mascota")
    print("2. Buscar codigo de la mascota")
    print("3. Buscar medicamentos para la mascota")
    print("4. Eliminar ficha de la mascota")
    print("5. Listar mascotas atendidas")
    print("6. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        nueva_ficha = ingresar_ficha()
        listado_mascotas = np.concatenate((listado_mascotas, nueva_ficha), axis=0)
        print("¡Ficha ingresada correctamente!")
    elif opcion == '2':
        codigo = input("Ingrese el CODIGO a buscar: ")
        mascota_encontrada = buscar_ficha_por_codigo(listado_mascotas, codigo)
        if mascota_encontrada is not None: 
            print(f"Nombre: {mascota_encontrada[0]}")
            print(f"codigo: {mascota_encontrada[2]}")
            print(f"edad: {mascota_encontrada[3]}")
            print(f"peso: {mascota_encontrada[4]}")
            print(f"diagnostico: {mascota_encontrada[5]}")
            print(f"Medicamentos: {mascota_encontrada[6]}")
        else:
            print("No se encontró ningún paciente con ese codigo.")

    elif opcion == '3':
        codigo = input("Ingrese el CODIGO para buscar medicamentos: ")
        buscar_medicamentos_por_codigo (listado_mascotas, codigo)

    elif opcion == '4':
        codigo = input("Ingrese el CODIGO de la ficha de la mascota a eliminar: ")
        listado_mascotas = eliminar_ficha(listado_mascotas, codigo)
        print("Ficha de la mascota eliminada correctamente.")

    elif opcion == '5':
        if len(listado_mascotas) > 0:
            print("Listado de pacientes atendidos:")
            listar_mascotas(listado_mascotas)
        else:
            print("No existen mascotas registradas.")

    elif opcion == '6':
        # Guardar los datos actualizados en el archivo JSON antes de salir
        guardar_datos(listado_mascotas)
        print("¡Estaremos esperando su proxima llegada!")
        break

    else:
        print("Opción invalida, ingrese una opción del 1 al 6.")