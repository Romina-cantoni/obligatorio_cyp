# 🎓 Obligatorio - Sistema de Gestión de Salas de Estudio (Base de Datos I - UCU)

Implementación de backend: python  
Framework (es un microframework en verdad): Flask  
Conexión a base de datos: MySQL  
  
Repo: https://github.com/Romina-cantoni/obligatorio_cyp.git  

------------------------ ORGANIZACIÓN DEL PROYECTO ------------------------

Elegimos simplificar el patrón MVC que implica Modelo-Vista-Controlador.  
Con la ayuda de la inteligencia artificial ordenamos correctamente las carpetas.  

obligatorio_cyp/  
├── controllers/  
├────── facultad_ctrl.py           
├── db/  
├────── connection.py       
├── routes/  
├────── api.py          
├── .env                   
├── app.py                  
├── README.md               
└── requirements.txt       
  
db/ centraliza la conexión a la base de datos.  
controllers/ contiene la lógica y validaciones.  
routes/ define los endpoints HTTP.  
app.py ejecuta el servidor.  
.env --> ACA VAN LAS CREDENCIALESS  
  
  
------------------------ .env FUNCIONALIDAD ------------------------  
  
Necesitamos la conexión con MySQL pero queríamos que los datos queden ocultos.  
En este caso investigamos sobre la funcionalidad del .env donde pusimos las credenciales.  
  
DB_HOST=127.0.0.1  
DB_USER=root  
DB_PASS=rootpassword  
DB_NAME=Gestion_Salas_UCU  
  
PASOS POR SI FALTAN INSTALACIONES:  
1. cd ~/Desktop/obligatorio_cyp  
2. python3 -m venv venv  
3. source venv/bin/activate  
4. pip install Flask mysql-connector-python python-dotenv  
5. pip freeze > requirements.txt  
