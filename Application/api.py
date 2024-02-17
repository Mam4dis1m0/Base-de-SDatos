from fastapi import APIRouter
import numpy
from Entity.estudiante import Estudiante
from DAL.estudiantes_repository import Estudiante


router = APIRouter()

@router.get("/obtener_todos")
def obtener_todos():
    return Estudiante

@router.get("/obtener_por_nombre")
def obtener_por_nombre(nombre):
    return next(filter(lambda estudiante: estudiante.nombre == nombre, Estudiante))

@router.post("/guardar_estudiante")
def guardar_estudiante(estudiante: Estudiante):
    Estudiante.append(estudiante)
    return "¡El estudiante ha sido guardado con éxito!"

@router.get("/filtrar")
def filtrar(calificacion: int):
    return [estudiante.nombre for estudiante in Estudiante if numpy.mean(estudiante.notas) >= calificacion]
