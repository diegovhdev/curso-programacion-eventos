# Editorial Andina S.A.S: Gestión Básica de Libros y Autores

## Información General

**Universidad**: Universidad del Valle, Caicedonia, Valle del Cauca  
**Curso**: Fundamentos de Programación Orientada a Eventos  
**Semestre**: 3er Semestre  
**Profesor**: Raúl Londoño Murillo  

**Estudiantes**:  
- Manuel Alejandro Borrero Sánchez  
- Keider Julián Chavarría Rojas  
- Juan Diego Valencia Hoyos  

**Proyecto Final**: Sistema de gestión básica de libros y autores.

---

## Tecnologías Utilizadas

- **Backend**: Django + Django REST Framework  
- **Frontend**: Python + Tkinter  
- **Respaldo Automático**: Hilos en segundo plano (`threading`)  
- **Formato de Respaldo**: Archivos `.txt` en texto plano  

---

## Requisitos del Sistema

- Python 3.10 o superior  
- Pip (administrador de paquetes)  
- Sistema operativo: Windows, macOS o Linux  

---

## Instalación del Proyecto

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/diegovhdev/curso-programacion-eventos
   ```
   Navegar a la subcarpeta `proyecto-final`.

2. **Crear un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate     # macOS/Linux
   .\env\Scripts\activate      # Windows
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos** (desde la carpeta del `proyecto-final/backend`):
   ```bash
   python manage.py migrate
   ```

---

## Ejecución del Proyecto

1. **Levantar el backend** (desde el directorio `proyecto-final/backend`):
   ```bash
   python manage.py runserver
   ```
   Esto inicia el API en: `http://127.0.0.1:8000/`

2. **Ejecutar la interfaz gráfica** (en otra terminal, desde el directorio `proyecto-final/frontend`):
   ```bash
   python __main__.py
   ```

---

## Funcionalidades

### Autores
- **Registro**:
  - Nombre
  - Nacionalidad
  - Edad
- **Consulta**: Individual o múltiple de autores registrados

### Libros
- **Registro**:
  - Título
  - Género
  - Páginas
  - Fecha de publicación (formato: `YYYY-MM-DD`)
- **Consulta**: Individual o múltiple de libros registrados

### Validación en Tiempo Real
- Cada campo se valida mientras el usuario ingresa datos.
- Mensajes de error si el formato es incorrecto o el campo está vacío.

### Respaldo Automático
- Se generan automáticamente cada 30 segundos mientras la aplicación está abierta:
  - `respaldo_autores.txt`
  - `respaldo_libros.txt`
- Los archivos se sobrescriben con cada respaldo.
- Se guardan en la misma carpeta donde se ejecuta la aplicación.
- Generados sin intervención del usuario mediante un hilo (`threading.Thread`) para no congelar la interfaz.

#### Ejemplo de Formato de Respaldo

**respaldo_autores.txt**:
```makefile
Nombre: Gabriel García Márquez
Nacionalidad: Colombiana
Edad: 87
```

**respaldo_libros.txt**:
```makefile
Título: Cien años de soledad
Género: Realismo Mágico
Páginas: 471
Fecha de publicación: 1967-05-30
```

---

## Estructura del Proyecto

```
├── __main__.py
├── modelos/
│   ├── modelo.py
│   ├── autor.py
│   └── libro.py
├── vistas/
│   ├── ventana_principal.py
│   ├── interfaz_formulario.py
│   └── tabla.py
├── controladores/
│   ├── comunicacion.py
│   └── validacion.py
```
