# 🛴 Práctica de POO: Sistema de Scooters Eléctricos

**Objetivo:** Comprender la estructura de un sistema orientado a objetos identificando clases, atributos, métodos, y diferenciando el "molde" (Clase) de la "realidad" (Objetos).

---

## 📖 1. El Caso de Estudio

Lee detenidamente la siguiente descripción de nuestro sistema:

> *"Estamos diseñando la lógica para una aplicación de renta de scooters en la ciudad. En nuestro sistema, cada **Scooter** tiene un número de identificación (ej. 'S-001'), un nivel de batería (del 0 al 100) y un estado que nos dice si está disponible para usarse o no. Los scooters pueden realizar tres acciones: desbloquearse para iniciar un viaje, terminar su viaje, y recargar su batería al 100%.*
> 
> *Por otro lado, tenemos al **Usuario**, que se registra con su nombre y mantiene un saldo de dinero en su cuenta. El usuario puede hacer dos cosas: agregar más saldo a su cuenta y rentar un scooter específico."*

---

## 🔍 2. Análisis (Diccionario de Clases)

💡 **TIP:** Los **Sustantivos** suelen ser Clases/Atributos. Los **Verbos** suelen ser Métodos.

### Entidad 1: `__________________`
**Atributos (Acceso privado `-`):**
* `- _________________ : ___________ ` *(identificador)*
* `- _________________ : ___________ ` *(batería)*
* `- _________________ : ___________ ` *(estado)*

**Métodos (Acceso público `+`):**
* `+ _________________() : boolean ` *(iniciar viaje)*
* `+ _________________() : void ` *(finalizar viaje)*
* `+ _________________() : void ` *(llenar batería)*

### Entidad 2: `__________________`
**Atributos (Acceso privado `-`):**
* `- _________________ : ___________ ` *(nombre)*
* `- _________________ : ___________ ` *(dinero)*

**Métodos (Acceso público `+`):**
* `+ _________________(monto: double) : void ` *(meter dinero)*
* `+ _________________(scooter: Scooter) : boolean ` *(usar scooter)*

---

## 📐 3. Diseño del Diagrama de Clases UML

Pasa la información de la sección anterior a un Diagrama de Clases formal (con sus tres bloques: Nombre, Atributos y Métodos). 

*(Puedes usar herramientas gratuitas como [Draw.io](https://app.diagrams.net/) para armarlo).*

---

## 🧩 4. De la Teoría a la Realidad (Objetos)

El diagrama es el "molde". Ahora define instancias reales asignando valores a los atributos.

**Objeto Scooter 1**
* `id = `
* `nivelBateria = `
* `estaDisponible = `

**Objeto Usuario 1**
* `nombre = `
* `saldo = `

---

## 🤔 Reflexión para discutir:
Si el **Objeto Usuario 1** intenta llamar al método `rentar()` utilizando un **Scooter** que tiene un 15% de batería, ¿qué debería hacer internamente tu código?
