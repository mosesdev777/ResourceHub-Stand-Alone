ResourceHub 🚀
ResourceHub es una aplicación web personal diseñada para guardar, organizar y redescubrir fácilmente los valiosos recursos de desarrollo (artículos, tutoriales, herramientas, librerías) que encuentras en internet. ¡Nunca más pierdas un enlace útil!

Este proyecto nació de la necesidad de tener un lugar centralizado para catalogar hallazgos, etiquetarlos por tecnología y propósito, y poder filtrarlos rápidamente cuando se necesiten.

📋 Tabla de Contenidos
✨ Características Principales

🛠️ Stack Tecnológico

⚙️ Instalación y Puesta en Marcha

🚀 Uso de la Aplicación

🤝 Contribuciones

📄 Licencia

👤 Autor

✨ Características Principales
Añadir Recursos: Guarda URLs con un título, descripción personalizada, tecnología y categoría.

Organización Inteligente: Asigna una tecnología principal (ej. Python, React) y una o más categorías (ej. Tutorial, Componente UI) a cada recurso.

Vista de Tarjetas: Visualiza tus recursos en una interfaz limpia y moderna.

Filtrado Potente: Encuentra rápidamente lo que buscas filtrando por tecnología o categoría.

Panel de Administración: Gestiona todas las entradas (recursos, tecnologías, categorías) fácilmente a través del panel de administrador de Django.

🛠️ Stack Tecnológico
Backend: Python, Django

Base de Datos: PostgreSQL

Frontend: HTML, CSS, JavaScript

Framework CSS: Bootstrap (potencialmente con Orbitron UI o MD Sketch para un estilo personalizado)

Entorno: Python Virtual Environment (venv)

⚙️ Instalación y Puesta en Marcha
Sigue estos pasos para tener una copia del proyecto corriendo en tu máquina local.

Prerrequisitos
Python 3.8+

PostgreSQL instalado y corriendo.

Git

Pasos
Clona el repositorio:

git clone https://github.com/tu-usuario/resource-hub-django.git
cd resource-hub-django

Crea y activa un entorno virtual:

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

Instala las dependencias:

pip install -r requirements.txt

(Nota: Asegúrate de crear un archivo requirements.txt con pip freeze > requirements.txt)

Configura la base de datos:

Crea una base de datos en PostgreSQL para el proyecto.

Copia el archivo .env.example a .env y rellena las variables de entorno, especialmente las de la base de datos (DB_NAME, DB_USER, DB_PASSWORD, etc.).

Aplica las migraciones:

python manage.py migrate

Crea un superusuario para acceder al panel de administración:

python manage.py createsuperuser

Ejecuta el servidor de desarrollo:

python manage.py runserver

¡Listo! La aplicación estará disponible en http://127.0.0.1:8000.

🚀 Uso de la Aplicación
Accede a la página principal para ver todos los recursos.

Usa los filtros para acotar tu búsqueda.

Haz clic en "Añadir Recurso" para guardar un nuevo enlace.

Navega a /admin e inicia sesión con tus credenciales de superusuario para gestionar las tecnologías y categorías disponibles.

🤝 Contribuciones
Por el momento, este es un proyecto personal. Sin embargo, si tienes ideas o sugerencias, no dudes en abrir un issue en el repositorio.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

👤 Autor
Moses Dev

Un desarrollador apasionado por el backend y la creación de herramientas útiles.

📺 YouTube: Moses Dev - Tutoriales sobre Python, Django, PHP, Laravel, SQL y mucho más.

🌐 Portafolio: (Añade aquí el enlace a tu portafolio)
