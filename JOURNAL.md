
## Overview

### Requirements

- Create a simple web application that charts sensor data in real-time

### Timeframe

- 1 Week, no more than 8 hours for both backend and frontend

### Identified Risks

- Limited experience with websockets
- Lack of experience with asyncio programming
- Lack of experience with Angular + TypeScript

### Guidelines

- Due to the limited timeframe focus only on minimal viable product features
- Reduce testing efforts minimum (unit tests, smoke tests)
- Use tools such as chatGPT to help deliver quickly a viable solution
- 5-6 hours max for the backend including web-sockets
- 5-6 hours max for the frontend including Grafana

### Milestones

- V0.0.1.0 - Backend with REST API without websockets
- V0.0.2.0 - Simple web app to poll the API
- V0.0.3.0 - Grafana integration and charting
- V0.0.4.0 - Add websockets to deliver real-time data
- V0.0.5.0 - Add optional features as requested in the documentation
- V0.0.6.0 - Add CI/CD pipeline with GitHub Actions

## Backend

The task assignment didn't specify the framework to use for the backend, so 
I decided to use Flask as I have more experience with it and it's easier to
setup and use for small projects. It offers also a simple way to integrate 
websockets and it's easy to test. The technology stack is as follows:

- Flask for REST API as WSGI application
- SQLAlchemy for database integration
- Websockets for real-time data production
- Postgres for data storage

The backend will be containerized with Docker and I will use a simple 
Dockerfile and docker-compose file to run the app. The application consists of 
two services: the Flask app and the Postgres database.

**Solution steps:**

1. Create a simple backend app with Flask with Docker (test Dockerfile)
2. Implement the seonsor data simulation (data logic) 
3. Add the routes with dummy data (routing logic)
4. Add the database integration with Postgres (database logic)
5. Test the REST API using the test client from Flask (integration)
6. Add websockets and implement the real-time data production (real-time)

**MVP features:**

- Dockerized Flask app
- Simulated sensor data stored in the database every 10 seconds
- REST API fetching sensor data from the database
- Tests for the REST API

**Extended features:**

- Websockets for real-time data production

**Time table:**

| Time | Task                                                  |
|------|-------------------------------------------------------|
| 0.5h | Setup the Flask app with Docker                       |
| 0.5h | Implement the sensor data simulation                  |
| 0.5h | Add the routes with dummy data and tests              |
| 1h   | Add the database integration with Postgres and tests  |
| 1h   | Add configuration using the instance folder and tests |
| 2h   | Review and research websockets                        |
| 0.5h | Documentation and cleanup before Tag V0.0.1.0         |

**Links:**
- https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html#summary
- https://flask.palletsprojects.com/en/stable/


## Frontend

Unfortunately, I don't have experience with Angular and TypeScript, so I will
use this opportunity to learn and implement a simple frontend app with Angular.
I will also use assisting tools such as chatGPT to help me deliver the solution
as quickly as possible. 

The technology stack is as follows:

- Angular for frontend
- TypeScript for the frontend logic
- Grafana for charting the data
- Any other libraries as needed

The frontend will be containerized with Docker and I will use a simple
Dockerfile and docker-compose file to run the app. The application consists of
two services: the Angular app and the Grafana service. The Grafana service 
offers a REST API that can be used to create dashboards, panels, and queries.

The following steps will be taken to implement the frontend:

1. Install node.js and Angular CLI
2. Install WebStorm and create a new Angular project
3. Follow the tutorial to create a simple Angular app
4. Implement a simple frontend app to poll the REST API
5. Dockerize the Angular app and update the docker-compose file
6. Integrate Grafana with the Angular app
7. Add a websockets service for real-time data consumption
8. Polish the frontend and add optional features
9. Add tests for the frontend app
10. Add CI/CD pipeline with GitHub Actions

**MVP features:**

- Dockerized Angular app
- Simple frontend app to poll the backend

**Extended features:**
- Grafana integration
- Websockets for real-time data consumption
- Optional features as requested in the documentation

**Timetable:**

| Time | Task                                                    |
|------|---------------------------------------------------------|
| 0.5h | 1) Install node.js and Angular CLI                      |
| 0.5h | 2) Install WebStorm and create a new Angular project    |
| 4h   | 3) Follow the tutorial to create a simple Angular app   |
| 1h   | 4) Implement a simple frontend app to poll the REST API |
| 0.5h | 5) Dockerize the Angular app and update the docker file |
| 0.5h | Documentation and Cleanup before tag V0.0.2.0           |


**Links:**
- https://angular.dev/tutorials/first-app
- https://blog.bouzekri.net/2017-11-03-debug-angular-app-in-webstorm.html
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- https://en.wikipedia.org/wiki/Bazel_(software)


## CI/CD

The CI/CD pipeline will be implemented using GitHub Actions. The pipeline will
consist of the following steps:

1. Linting and code quality checks
2. Unit tests for the backend and frontend
3. Build the Docker images
4. Push the Docker images to the Docker Hub

