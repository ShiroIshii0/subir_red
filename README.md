# 📚 Proyecto Django - Plataforma de Intercambio de Libros 
Este proyecto es una plataforma web para la gestión e intercambio de libros físicos entre usuarios. Permite a cualquier persona registrar, intercambiar y gestionar libros de forma sencilla y segura.
---

## ✅ Requisitos

- Python 3.11 o superior
- pip
- Entorno virtual (recomendado)

---
## 🚀 Pasos para la instalación

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd avance_proyecto
```

### 2. Crear y activar el entorno virtual

```bash
# En Windows
python -m venv env
pip install -r requirements.txt
env\Scripts\activate

# En Linux/Mac
python3 -m venv env
pip install -r requirements.txt
source env/bin/activate
```
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Iniciar servidor: `python manage.py runserver
