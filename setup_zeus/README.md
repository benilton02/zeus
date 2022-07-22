# zeus
### Description
The service ZEUS was designed and built to collect data from an Open Weather API and store it as JSON data.

The stored data are:
- User defined ID (unique)
- Datetime of request
- City ID
- Temperature in Celsius
- Humidity

### Requirements

- Python ^3.9
- Docker [more informations](https://docs.docker.com/engine/install/) 
- Docker compose [more informations](https://docs.docker.com/compose/install/) 

### How to run in Docker?
 On Linux, enter into project folder. Copy and paste the command below:
 
 ```sh
 docker compose up --build
 ```
### How to see API ZEUS documenation?
- Ensure the zeus_container is running;
- Swagger [docs](http://0.0.0.0:8000/swagger/) 
- Redoc [docs](http://0.0.0.0:8000/redoc/) 
