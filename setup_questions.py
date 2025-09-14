#!/usr/bin/env python3
"""
Script para configurar las preguntas del administrador
"""
import json
import os
from __init__ import create_app

def setup_questions():
    """Configura las preguntas del administrador"""
    app = create_app()
    
    with app.app_context():
        try:
            questions_path = 'questions_admin.json'
            
            # Verificar si el archivo existe
            if os.path.exists(questions_path):
                print(f"✅ Archivo {questions_path} ya existe")
                with open(questions_path, 'r', encoding='utf-8') as f:
                    questions = json.load(f)
                print(f"📋 Preguntas actuales: {len(questions)} preguntas")
                return
            
            # Crear archivo con preguntas completas
            questions = [
                {
                    "name": "role",
                    "type": "select",
                    "label": "¿Cuál es tu rol en el establecimiento educativo?",
                    "choices": ["profesor", "director", "asistente"]
                },
                {
                    "name": "school_type",
                    "type": "select",
                    "label": "¿En qué tipo de establecimiento trabajas?",
                    "choices": ["rural", "urbana", "cientifico-humanista", "tecnico-profesional"]
                },
                {
                    "name": "dependency",
                    "type": "select",
                    "label": "¿Cuál es la dependencia de tu establecimiento?",
                    "choices": ["municipal", "privada-subvencionada", "privada-pagada"]
                },
                {
                    "name": "age_range",
                    "type": "select",
                    "label": "¿En qué rango de edad te encuentras?",
                    "choices": ["20-30", "31-40", "41-50", "51+"]
                },
                {
                    "name": "digital_tools_skill",
                    "type": "select",
                    "label": "Evalúa tu habilidad con herramientas TI básicas (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "advanced_tic_skill",
                    "type": "select",
                    "label": "Evalúa tu habilidad con TIC avanzadas (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "digital_citizenship_skill",
                    "type": "select",
                    "label": "Evalúa tu conocimiento sobre ciudadanía digital (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "teaching_tech_skill",
                    "type": "select",
                    "label": "Evalúa tu habilidad para usar tecnología en la enseñanza (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "leadership_support",
                    "type": "select",
                    "label": "Evalúa el apoyo del liderazgo institucional en tecnología (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "resource_support",
                    "type": "select",
                    "label": "Evalúa los recursos tecnológicos disponibles (1-5)",
                    "choices": ["1", "2", "3", "4", "5"]
                },
                {
                    "name": "interest_digital_literacy",
                    "type": "boolean",
                    "label": "¿Te interesa la alfabetización digital?"
                },
                {
                    "name": "interest_educational_innovation",
                    "type": "boolean",
                    "label": "¿Te interesa la innovación educativa?"
                },
                {
                    "name": "interest_leadership",
                    "type": "boolean",
                    "label": "¿Te interesa el liderazgo?"
                },
                {
                    "name": "learning_format",
                    "type": "select",
                    "label": "¿Qué formato de aprendizaje prefieres?",
                    "choices": ["en-linea", "talleres", "autoaprendizaje"]
                }
            ]
            
            # Guardar archivo
            with open(questions_path, 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Archivo {questions_path} creado con {len(questions)} preguntas")
            
            # Verificar que se guardó correctamente
            with open(questions_path, 'r', encoding='utf-8') as f:
                loaded_questions = json.load(f)
            print(f"✅ Verificación: {len(loaded_questions)} preguntas cargadas correctamente")
            
        except Exception as e:
            print(f"❌ Error configurando preguntas: {e}")
            raise

if __name__ == "__main__":
    setup_questions()
