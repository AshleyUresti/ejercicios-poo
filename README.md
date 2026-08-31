# GUÍA DE POO EN PYTHON
Encontrarás un espacio de aprendizaje para entender cómo funciona este mundo en uno de los lenguajes más usadas actualmente.
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/VVANEGZ/ejercicios-poo)

Actividad 01. "¿Cómo abstraer algo del mundo real a la programación?"
---------------------------------------------------------------------
Caso de estudio: sistema de scooters eléctricos.

Descripción: En el sistema que se requiere diseñar, cada scooter cuenta con:
- número de identificación (ej. 'S-001'),
- nivel de batería (del 0 al 100)
- estado lógico que indica si está disponible para usarse o no

  Acciones que puede realizar:
  - desbloquearse para iniciar un viaje
  - terminar el viaje
  - recargar batería al 100%
 
La entidad usuario: 
- se registra con su nombre
- mantiene un saldo monetario en su cuenta

  Acciones operativas:
  - agregar más saldo a su cuenta
  - rentar un scooter específico
 -------------------------------------------------------------------
 Diagramas UML en draw.io
 
 Entidad 1:
 
 <img width="331" height="312" alt="image" src="https://github.com/user-attachments/assets/17a04cc8-4996-45ce-8a51-021a9ec7c515" />

 Entidad 2:
 
 <img width="419" height="248" alt="image" src="https://github.com/user-attachments/assets/4fa03f7a-217b-4b64-80fb-a58dbd5ad808" />

 -------------------------------------------------------------------
Definir instancias en memoria

Scooter 1:
- id = "S-007"
- bateria = 67
- estaDisponible = true

Usuario 1:
- nombre = "Mein"
- saldo = 122.50
-------------------------------------------------------------------
Pregunta de análisis lógico

Si la instancia de Usuario 1 intenta ejecutar el método rentar() enviando como parámetro un Scooter que tiene un 15% de batería, ¿cómo debería comportarse internamente la lógica del sistema?

En ese caso, habría que hacer pequeños ajustes en el código, porque se tendría que verificar que el scooter cuente con un mínimo de batería para ser rentado, además de la disponibilidad, ya que no sería seguro que el usuario lo rente en esas condiciones. Para integrar ese caso, en el método rentar() se agregaría una serie de if que devuelvan true sólo si el scooter está disponible y si cuenta con el mínimo de batería para no dejar tirado al usuario.

Uso de IA:
No recurrí a la ayuda de IA directamente, ya que solo consulté en internet algunas reglas de nomenclatura para escribir correctamente en el diccionario de clases y pasarlo al diagrama UML, así como información sobre los tipos de datos para elegir el correcto. Me resultó un ejercicio muy interesante sobre todo por la pregunta lógica del final.

-------------------------------------------------------------------

EVIDENCIASS

<img width="1920" height="1080" alt="Captura de pantalla (183)" src="https://github.com/user-attachments/assets/0ff389ae-3fc9-440b-99d9-12a68a745d4a" />

<img width="1920" height="1080" alt="Captura de pantalla (184)" src="https://github.com/user-attachments/assets/9c264c00-0ef6-41e8-bd36-6f2d1736e60d" />

<img width="1920" height="1080" alt="Captura de pantalla (185)" src="https://github.com/user-attachments/assets/fb7c610d-b4d0-48a2-ae32-dee5ba792b71" />

<img width="1920" height="1080" alt="Captura de pantalla (186)" src="https://github.com/user-attachments/assets/54b19261-d986-4ba7-9bf6-0586880084a5" />

<img width="1920" height="1080" alt="Captura de pantalla (188)" src="https://github.com/user-attachments/assets/338fce02-8bb0-48ee-bbd5-66d17c569b27" />


