# Sidecar Pattern Example

This project demonstrates the Sidecar Pattern using Docker, where a primary application container communicates with a sidecar container for log processing. The primary application is a Flask server, and the sidecar processes the application's logs.

[Ir a la sección en español](#ejemplo-de-patr%C3%B3n-sidecar)

---

## **Getting Started**

### **Prerequisites**

1. Install Docker:
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)

2. Clone this repository:
   ```bash
   git clone https://github.com/Osc2405/Sidecar_Pattern_Example.git
   cd Sidecar_Pattern_Example
   ```

---

## **File Structure**
```
Sidecar_Pattern_Example/
├── app/                  # Flask application code
│   ├── app.py            # Main Flask app file
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Dockerfile for Flask app
└── README.md             # Project documentation
```

---

## **Steps to Run the Project**

1. **Build and Start Containers**
   Run the following command to build the Docker images and start the containers:
   ```bash
   docker-compose up --build
   ```

2. **Access the Flask Application**
   - Open your browser and go to:
     ```
     http://localhost:5000
     ```

3. **Check Logs**
   - Logs are processed by the sidecar container and displayed in the terminal.

---

## **Endpoints**

| Endpoint | Description             |
|----------|-------------------------|
| `/`      | Returns "Hola, mundo! Revisa los logs para más detalles." |

---

## **Important Notes**

1. **Volume Sharing**:
   - Logs are shared between the `app` and `log-processor` containers using Docker volumes.

2. **Logs Location**:
   - The `app.log` file is located in the shared volume, accessible by both containers.

---

## **Stop and Remove Containers**

To stop the running containers and remove associated resources:
```bash
docker-compose down
```

---

## **Contributing**

Feel free to fork this repository, create a feature branch, and submit a pull request. For major changes, open an issue first to discuss the proposed changes.

---

# Ejemplo de Patrón Sidecar

[Ir a la sección en inglés](#Sidecar_Pattern_Example)

Este proyecto demuestra el patrón Sidecar utilizando Docker, donde un contenedor de aplicación principal se comunica con un contenedor sidecar para procesar registros. La aplicación principal es un servidor Flask, y el sidecar procesa los registros de la aplicación.

---

## **Cómo Empezar**

### **Requisitos Previos**

1. Instalar Docker:
   - [Guía de Instalación de Docker](https://docs.docker.com/get-docker/)

2. Clonar este repositorio:
   ```bash
   git clone https://github.com/Osc2405/Sidecar_Pattern_Example.git
   cd Sidecar_Pattern_Example
   ```

---

## **Estructura de Archivos**
```
Sidecar_Pattern_Example/
├── app/                  # Código de la aplicación Flask
│   ├── app.py            # Archivo principal de la aplicación Flask
│   └── requirements.txt  # Dependencias de Python
├── docker-compose.yml    # Configuración de Docker Compose
├── Dockerfile            # Dockerfile para la aplicación Flask
└── README.md             # Documentación del proyecto
```

---

## **Pasos para Ejecutar el Proyecto**

1. **Construir e Iniciar los Contenedores**
   Ejecuta el siguiente comando para construir las imágenes de Docker e iniciar los contenedores:
   ```bash
   docker-compose up --build
   ```

2. **Acceder a la Aplicación Flask**
   - Abre tu navegador y ve a:
     ```
     http://localhost:5000
     ```

3. **Verificar los Registros**
   - Los registros son procesados por el contenedor sidecar y se muestran en la terminal.

---

## **Endpoints**

| Endpoint | Descripción             |
|----------|-------------------------|
| `/`      | Devuelve "Hola, mundo! Revisa los logs para más detalles." |

---

## **Notas Importantes**

1. **Compartición de Volúmenes**:
   - Los registros se comparten entre los contenedores `app` y `log-processor` utilizando volúmenes de Docker.

2. **Ubicación de los Registros**:
   - El archivo `app.log` se encuentra en el volumen compartido, accesible por ambos contenedores.

---

## **Detener y Eliminar Contenedores**

Para detener los contenedores en ejecución y eliminar los recursos asociados:
```bash
docker-compose down
```

---

## **Contribuciones**

Siéntete libre de bifurcar este repositorio, crear una rama de características y enviar una solicitud de incorporación de cambios (pull request). Para cambios importantes, abre primero un issue para discutir las propuestas.
