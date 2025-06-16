#Diagramas del proyecto: Generador de contraseñas
En esta carpeta se encuentran los diagramas utilizados para el edsarrollo del proyecto de generación de contraseñas seguro.

#Diagrama de flujo.
Este diagrama representa el proceso lógico que sigue el generador de contraseñas: 
- Solicita al usuario la longitud deseada.
- Pregunta qué tipos de caracteres desea incluir (mayúsculas, minpusculas, número y símbolos.)
- Valida las selecciones y genera una contraseña que cumpla con los criterios solicitados.
- Si no se cumplen los criterios se repite el proceso.
![diagrama de flujo actualizado__page-0001](https://github.com/user-attachments/assets/6d80474b-26a6-4dd1-acdb-479611ff18f3)

  #Diagrama de Arquitectura
  Este diagrama muestra los componentes estructurales del sistema y como interactúan:
  - La interfaz UI se comunica con la API.
  - La API maneja la lógica del generador de contraseñas y envía logs.
  - Módulos como el validador de entradas, selector de caracteres y validador de requisitos se conectan al núcleo.
  - Toda la lógica puede interactuar con una base de datos si es necesario.![diagrama de arquitectura](https://github.com/user-attachments/assets/ee1add9a-44af-431b-9d3d-5dadce5c518b)
