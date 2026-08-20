# Práctica de Programación Orientada a Objetos: Sistema de Scooters Eléctricos

**Objetivo:** Comprender la estructura de un sistema orientado a objetos identificando clases, atributos y métodos, diferenciando el concepto abstracto (Clase) de su implementación (Objeto).

---

## 1. El Caso de Estudio

![Scooter Eléctrico en la ciudad](https://images.unsplash.com/photo-1593697821252-0c9137d9fc45?auto=format&fit=crop&w=800&q=80)
*Figura 1: Sistema urbano de movilidad eléctrica.*

Lee detenidamente la siguiente descripción del requerimiento:

> "Se requiere diseñar la lógica para una aplicación de renta de scooters. En el sistema, cada **Scooter** cuenta con un número de identificación (ej. 'S-001'), un nivel de batería (del 0 al 100) y un estado lógico que indica si está disponible para usarse o no. Los scooters pueden ejecutar tres acciones: desbloquearse para iniciar un viaje, terminar su viaje, y recargar su batería al 100%.
> 
> Por otro lado, la entidad **Usuario** se registra con su nombre y mantiene un saldo monetario en su cuenta. El usuario puede realizar dos acciones operativas: agregar más saldo a su cuenta y rentar un scooter específico."

---

## 2. Análisis y Diccionario de Clases

**Nota:** En el análisis de requerimientos, los sustantivos suelen representar Clases o Atributos, mientras que los verbos representan Métodos. Completa la siguiente estructura considerando los tipos de datos adecuados.

### Entidad 1: `__________________`
**Atributos (Acceso privado `-`):**
* `- _________________ : ___________ ` (identificador)
* `- _________________ : ___________ ` (batería)
* `- _________________ : ___________ ` (estado de disponibilidad)

**Métodos (Acceso público `+`):**
* `+ _________________() : boolean ` (iniciar viaje)
* `+ _________________() : void ` (finalizar viaje)
* `+ _________________() : void ` (llenar batería)

### Entidad 2: `__________________`
**Atributos (Acceso privado `-`):**
* `- _________________ : ___________ ` (nombre)
* `- _________________ : ___________ ` (dinero)

**Métodos (Acceso público `+`):**
* `+ _________________(monto: double) : void ` (agregar saldo)
* `+ _________________(scooter: Scooter) : boolean ` (rentar scooter)

---

## 3. Diseño del Diagrama de Clases UML

A partir de la información estructurada en la sección anterior, elabora un Diagrama de Clases formal. Asegúrate de incluir los tres bloques estándar: Nombre de la clase, Atributos y Métodos con sus respectivos parámetros y valores de retorno.

*(Se recomienda utilizar la herramienta Draw.io para generar el diagrama y adjuntar la imagen resultante en esta sección de su documento).*

---

## 4. Instanciación (De la Teoría a la Realidad)

El diagrama de clases funciona como un molde estructural. A continuación, define instancias en memoria asignando valores concretos a los atributos.

**Instancia de Scooter 1**
* `id = `
* `nivelBateria = `
* `estaDisponible = `

**Instancia de Usuario 1**
* `nombre = `
* `saldo = `

---

## Pregunta de Análisis Lógico
Si la Instancia de Usuario 1 intenta ejecutar el método `rentar()` enviando como parámetro un Scooter que tiene un 15% de batería, ¿cómo debería comportarse internamente la lógica del sistema? Justifica tu respuesta.
