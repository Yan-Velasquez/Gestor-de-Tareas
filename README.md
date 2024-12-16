# Gestión de Tareas

Este proyecto es una aplicación de gestión de tareas desarrollada con Streamlit y SQLAlchemy. Permite agregar, listar, completar, eliminar, exportar e importar tareas desde un archivo JSON.

## Características

- **Agregar Tareas**: Permite agregar nuevas tareas con un título y una descripción.
- **Listar Tareas**: Muestra todas las tareas existentes con su estado (Pendiente o Completada).
- **Completar Tareas**: Permite marcar tareas como completadas.
- **Eliminar Tareas Completadas**: Elimina todas las tareas que han sido marcadas como completadas.
- **Exportar Tareas a JSON**: Exporta todas las tareas a un archivo JSON.
- **Importar Tareas desde JSON**: Importa tareas desde un archivo JSON.

## Requisitos

- Python 3.10 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/Yan-Velasquez/Gestor-de-Tareas.git
    cd Gestor-de-Tareas
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv env
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
5. Instalación de librerias
    ```sh
    pip install streamlit
    pip install sqlalchemy
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    streamlit run task_app.py
    ```

2. Abre tu navegador web y ve para interactuar con la aplicación.
- En la primera vista de Agregar Tarea, podras agregar el título y su descripción.
 ![image](https://github.com/user-attachments/assets/aa794b7f-433b-4d33-a8a8-9cae0ac1345b)


- En la vista de ver Tareas, podrás ver todas las tareas con su título, descripción y estado.
- La opción de exportar las tareas en un archivo JSON mediante un botón.
- Poder Eliminar las tareas completadas mediante un botón.
- Importar tareas desde un archivo JSON.
- Cuando seleccionas la casilla de checkbox se actualiza el estado de la tarea a realizado

![image](https://github.com/user-attachments/assets/fc78eb7e-8e31-4526-9f23-d3fcdc3a1841)


