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
├────── participante_ctrl.py           
├── db/  
├────── connection.py       
├── routes/  
├────── api.py          
├── .env                   
├── app.py                  
├── main.py                  
├── README.md               
└── requirements.txt       
  
db/ centraliza la conexión a la base de datos.  
controllers/ contiene la lógica y validaciones.
- principalmente las operaciones CRUD   
routes/ define los endpoints HTTP.  
app.py ejecuta el servidor.  
.env --> ACA VAN LAS CREDENCIALESS  
  
------------------------ COMO CREAR LA BASE DE DATOS ------------------------  

En el doc a continuación se podrá ver la creación de tablas y las inserciones mínimas para la base de datos.

PASO IMPORTANTE:

CREATE DATABASE IF NOT EXISTS Gestion_Salas_UCU;
USE Gestion_Salas_UCU;

https://docs.google.com/document/d/1uZsGdnZJ-oZtIWSjVWLlQIzFK8s3bMD0BKRyKQusuO4/edit?usp=sharing
  
A CONTINUACIÓN las credenciales necesarias para la conexión.

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


Ultimas modificaciones 31/10/2025:  
- creacion de consultas en SQL (falta transferir para python en el archivo reportres_Ctrl, ya hay un ejemplo de como hacerlo)  
- Main y funcionalidad con consola sobre CRUD de usuarios, practicamente abm (ver si cambia en algo).  
- Implementacion de un menu, creo que va a ser mas facil pasarlo a interfaz grafica si llegamos :).  



