# CASO DE ESTUDIO: Biblioteca UN

## 1. Actores (Descripción)
*   **Estudiante:** Usuario, matriculado en pregrado/posgrado que pide libros prestados.
*   **Profesor:** Usuario, afiliado a alguna facultad, que pide libros prestados o material de apoyo.
*   **Bibliotecario:** Administrador del sistema de préstamos e inventario.

## 2. Clases (Atributos y Métodos)

**Persona**
*   Atributos:
    *   `String` nombre
    *   `String` cedula
    *   `String` correo
    *   `String` telefono
    *   `boolean` estadoElegible
*   Métodos:
    *   `Persona()`
    *   `registrar()`
    *   `actualizar()`
    *   `solicitarPrestamo()`
    *   `devolverLibro()`
    *   `getters()`
    *   `setters()`

**Estudiante**
*   Atributos:
    *   `String` codigoEstudiantil
    *   `String` carrera
*   Métodos:
    *   `Estudiante()`
    *   `renovarPrestamo()`
    *   `consultarMultas()`
    *   `getters()`
    *   `setters()`

**Profesor**
*   Atributos:
    *   `String` facultad
    *   `String` tipoVinculacion
*   Métodos:
    *   `Profesor()`
    *   `solicitarReservaProlongada()`
    *   `pedirMaterialApoyo()`
    *   `getters()`
    *   `setters()`

**Bibliotecario**
*   Atributos:
    *   `Biblioteca` biblioteca
*   Métodos:
    *   `Bibliotecario()`
    *   `autorizarPrestamo()`
    *   `auditarInventario()`
    *   `actualizarInventario()`
    *   `getters()`
    *   `setters()`

**Biblioteca**
*   Atributos:
    *   `Inventario` inventario
    *   `String` tematica
    *   `Bibliotecario[]` bibliotecarios
    *   `String` ubicacion
*   Métodos:
    *   `Biblioteca()`
    *   `consultarHorario()`
    *   `generarReporte()`
    *   `getters()`
    *   `setters()`

**Inventario**
*   Atributos:
    *   `Ejemplar[]` ejemplares
    *   `int` cantidad
    *   `String` ubicacion
*   Métodos:
    *   `Inventario()`
    *   `ingresarEjemplar()`
    *   `retirarEjemplar()`
    *   `getters()`
    *   `setters()`

**Libro**
*   Atributos:
    *   `String` autor
    *   `String` titulo
    *   `Date` fechaPublicacion
    *   `Persona` poseedor
    *   `String` isbn
    *   `String` idioma
    *   `String` estado
*   Métodos:
    *   `Libro()`
    *   `verificarDisponibilidad()`
    *   `getters()`
    *   `setters()`

**Ejemplar**
*   Atributos:
    *   `Libro` libro
    *   `String` codigoBarras
    *   `String` estado
    *   `String` ubicacion
*   Métodos:
    *   `Ejemplar()`
    *   `cambiarEstado()`
    *   `verificarDisponibilidad()`
    *   `getters()`
    *   `setters()`

**Prestamo**
*   Atributos:
    *   `Persona` persona
    *   `Ejemplar` ejemplar
    *   `Date` fechaInicio
    *   `Date` fechaVencimiento
    *   `Date` fechaDevolucion
    *   `String` estado
*   Métodos:
    *   `Prestamo()`
    *   `registrarDevolucion()`
    *   `estaVencido()`
    *   `calcularDiasMora()`
    *   `getters()`
    *   `setters()`

**Multa**
*   Atributos:
    *   `Persona` persona
    *   `Prestamo` prestamo
    *   `double` valor
    *   `String` motivo
    *   `String` estado
    *   `Date` fechaGeneracion
*   Métodos:
    *   `Multa()`
    *   `calcularMulta()`
    *   `pagar()`
    *   `estaPagada()`
    *   `getters()`
    *   `setters()`

## 3. Relaciones
*   **Herencia:** Persona -> Bibliotecario
*   **Herencia:** Persona -> Estudiante
*   **Herencia:** Persona -> Profesor
*   **Asociación:** Bibliotecario `0..*` -> Biblioteca `1`
*   **Agregación/Composición:** Biblioteca `1` -> Inventario `1`
*   **Agregación/Composición:** Inventario `1` -> Ejemplar `0..*`
*   **Asociación:** Ejemplar `0..*` -> Libro `1`
*   **Asociación:** Persona `1` -> Prestamo `0..*`
*   **Asociación:** Ejemplar `1` -> Prestamo `0..*`
*   **Asociación:** Persona `1` -> Multa `0..*`
*   **Asociación:** Prestamo `1` -> Multa `0..1`

## 4. Conceptos OOP
*   **Encapsulamiento:** Los atributos son `private` y se accede a ellos mediante getters y setters `public`.
*   **Herencia:** `Estudiante`, `Profesor` y `Bibliotecario` reutilizan los atributos y métodos comunes definidos en `Persona`.
*   **Polimorfismo:** Una referencia de `Persona` puede representar un `Estudiante`, un `Profesor` o un `Bibliotecario`. Los métodos heredados, como `solicitarPrestamo()`, pueden sobrescribirse para aplicar reglas diferentes según el tipo de persona.
*   **Abstracción:** `Libro` representa la información bibliográfica, `Ejemplar` una copia física, `Prestamo` el préstamo y `Multa` una sanción. Cada clase expone solo las operaciones relacionadas con su responsabilidad.
