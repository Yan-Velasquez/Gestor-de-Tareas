# PROGRAMA PARA LA GESTIÓN DE TAREAS
# Este programa permite gestionar tareas, permitiendo agregar, listar, completar y eliminar tareas.
# También permite exportar e importar tareas desde un archivo JSON.

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, exc
import json
import pandas as pd


# Crear base y configuración
Base = declarative_base()

class Tarea(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Boolean, default=False)  # False = Pendiente, True = Completada

# Crear conexión a la base de datos SQLite
engine = create_engine('sqlite:///taks.db')
Base.metadata.create_all(engine)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


# Agregar tarea
def agregar_tarea(titulo, descripcion):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    return "Tarea agregada correctamente."

def l_tareas():
    return session.query(Tarea).all()

def eliminar_tareas_completadas():
    session.query(Tarea).filter_by(estado=True).delete()
    session.commit()
    return "Tareas completadas eliminadas."

def guardar_tareas_en_json(filename):
    tareas = l_tareas()
    with open(filename, 'w') as f:
        json.dump([{
            'id': tarea.id,
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'estado': tarea.estado
        } for tarea in tareas], f)
    return "Tareas exportadas a JSON."
