from Task_Project import agregar_tarea, eliminar_tareas_completadas, guardar_tareas_en_json
import streamlit as st
import json
from Task_Project import Tarea, session, l_tareas
import pandas as pd

# Interfaz principal
st.title("Gestión de Tareas")

# Usamos `st.radio` para el menú, creando una interfaz de pestañas
opcion = st.radio(" ", ["Agregar Tarea", "Ver Tareas"])


if opcion == "Agregar Tarea":
    titulo = st.text_input("Título")
    descripcion = st.text_area("Descripción")
    if st.button("Agregar"):
        if titulo and descripcion:
            st.success(agregar_tarea(titulo, descripcion))
        else:
            st.error("Por favor, completa todos los campos.")
            
elif opcion == "Ver Tareas":

    # Listar todas las tareas (debe devolver objetos del modelo Tarea)
    tareas = l_tareas()

    if not tareas:  # Manejar el caso cuando no hay tareas
        st.info("No hay tareas para mostrar.")
    else:
        # Crear los encabezados
        cols = st.columns([0.1, 0.4, 0.4, 0.4])  # Las proporciones de las columnas
        cols[1].subheader("Título")  
        cols[2].subheader("Descripción")  
        cols[3].subheader("Estado") 


        # Crear una estructura de tabla y agregar checkbox para cada tarea
        for tarea in tareas:
            if isinstance(tarea, Tarea):  # Verificar que sea una instancia del modelo Tarea
                cols = st.columns([0.1, 0.4, 0.4, 0.3])  # 4 columnas: checkbox, título, descripción, y estado
        
                # Columna del checkbox
                estado_actualizado = cols[0].checkbox("", value=tarea.estado, key=f"checkbox_{tarea.id}")

                # Columna del título
                cols[1].text(tarea.titulo)

                # Columna de la descripción
                cols[2].text(tarea.descripcion)
                
                # Columna del estado
                estado_texto = "Completada" if estado_actualizado else "Pendiente"
                cols[3].text(estado_texto)
                
                # Si el checkbox cambia su estado, actualizamos en la base de datos
                if estado_actualizado != tarea.estado:  # Cambió el estado
                    tarea.estado = estado_actualizado  # Actualizamos el estado local
                    session.commit()  # Guardamos el cambio en la base de datos
                    st.rerun()  # Refrescamos la página para reflejar los cambios
            else:
                st.error("Los datos no coinciden con el modelo esperado.")
    
    st.subheader(" ")
    col1, col2, col3 = st.columns(3)
    
    with col1:         
        if st.button("Exportar a JSON"):
            filename = "tareas.json"
            st.success(guardar_tareas_en_json(filename))

            
    # Manejar estado del uploader y su visibilidad
    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = 0  # Estado inicial para controlar el reseteo
    with st.expander("Importar archivo JSON"):
        # Mostrar el uploader
        uploaded_file = st.file_uploader(
            "Selecciona un archivo JSON",
            type=["json"],
            key=f"uploader_{st.session_state.uploader_key}"  # Clave dinámica para reinicialización
        )        
    
    if uploaded_file is not None:
        try:
            # Convertir el archivo en un objeto manejable
            tareas_json = uploaded_file.read().decode("utf-8")
            tareas = json.loads(tareas_json)
            #st.success("Tareas importadas:", tareas)
        
            for t in tareas:
                # Crear un nuevo objeto `Tarea` basado en los datos JSON
                nueva_tarea = Tarea(
                    id=t.get('id', None),  # Usar `None` si no está presente el ID
                    titulo=t['titulo'],
                    descripcion=t['descripcion'],
                    estado=t['estado']
                )
                session.merge(nueva_tarea)
                session.commit()
                
                # Resetear el uploader incrementando su clave
                st.session_state.uploader_key += 1              
            
            st.rerun()
            st.success("Tareas importadas correctamente.")
            
        except json.JSONDecodeError as e:
            st.error(f"Error al decodificar el JSON: {e}")
        except Exception as e:
            st.error(f"Error al importar tareas: {e}")

        
        
    with col3: 
        if st.button("Eliminar Completadas"):
            st.success(eliminar_tareas_completadas())
            st.rerun()
    
