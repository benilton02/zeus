# zeus
### Description
This API was design and built to collect data from an [Open Weather API](https://openweathermap.org/) and store it as a JSON data.

### Dependencies
- Python 3.9^
- Docker Engine. [Info](https://docs.docker.com/engine/install/)
- Docker Compose. [Info](https://docs.docker.com/compose/install/)

### How to Run in Docker
On Linux, Copy and paste the command bellow:
```sh
docker-compose up --build
```
or

```sh
docker compose up --build
```


 ### How to access Swagger local:
 - The container must be running
 - Access: [http://0.0.0.0:8000/swagger/](http://0.0.0.0:8000/swagger/)