# Práctica de Programación Orientada a Objetos: Sistema de Scooters Eléctricos

**Objetivo:** Comprender la estructura de un sistema orientado a objetos identificando clases, atributos y métodos, diferenciando el concepto abstracto (Clase) de su implementación (Objeto).

---

## Paso 1: Lectura del Caso de Estudio

**Lee detenidamente la siguiente descripción del requerimiento para identificar las entidades principales del sistema.**

> "Se requiere diseñar la lógica para una aplicación de renta de scooters. En el sistema, cada **Scooter** cuenta con un número de identificación (ej. 'S-001'), un nivel de batería (del 0 al 100) y un estado lógico que indica si está disponible para usarse o no. Los scooters pueden ejecutar tres acciones: desbloquearse para iniciar un viaje, terminar su viaje, y recargar su batería al 100%.
> 
> Por otro lado, la entidad **Usuario** se registra con su nombre y mantiene un saldo monetario en su cuenta. El usuario puede realizar dos acciones operativas: agregar más saldo a su cuenta y rentar un scooter específico."

---

## Paso 2: Análisis y Diccionario de Clases

**Completa la siguiente estructura identificando los atributos y métodos. Recuerda que los sustantivos suelen representar Clases o Atributos, mientras que los verbos representan Métodos. Utiliza los modificadores de acceso y tipos de datos adecuados en cada línea vacía.**

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

## Paso 3: Diseño del Diagrama de Clases UML

**A partir de la información estructurada en el paso anterior, elabora un Diagrama de Clases formal. Asegúrate de incluir los tres bloques estándar (Nombre de la clase, Atributos y Métodos) y adjuntar la captura o imagen del diagrama resultante en tu documento.**

*(Herramienta sugerida: Draw.io)*

---

## Paso 4: Instanciación (De la Teoría a la Realidad)

**El diagrama de clases funciona como un molde estructural. A continuación, define instancias en memoria asignando valores concretos a los atributos de cada objeto para ejemplificar su estado.**

**Instancia de Scooter 1**
* `id = `
* `nivelBateria = `
* `estaDisponible = `

**Instancia de Usuario 1**
* `nombre = `
* `saldo = `

---

## Paso 5: Pregunta de Análisis Lógico

**Justifica tu respuesta a la siguiente interrogante lógica basándote en los conceptos de POO estudiados:**

Si la Instancia de Usuario 1 intenta ejecutar el método `rentar()` enviando como parámetro un Scooter que tiene un 15% de batería, ¿cómo debería comportarse internamente la lógica del sistema? 

---

> [!IMPORTANT]
> <span style="color: #d32f2f; font-weight: bold; font-size: 1.1em;">INSTRUCCIONES DE ENVÍO: Copia todo el contenido de esta página en un documento de Word o Google Docs, resuelve los espacios en blanco, pega la imagen de tu diagrama UML en el Paso 3 y envía el archivo final en formato PDF a través de la plataforma oficial para su revisión.</span>
