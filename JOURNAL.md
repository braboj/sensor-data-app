
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

**Time journal:**

| Time | Task                                                  |
|------|-------------------------------------------------------|
| 0.5h | Setup the Flask app with Docker                       |
| 0.5h | Implement the sensor data simulation                  |
| 0.5h | Add the routes with dummy data and tests              |
| 1h   | Add the database integration with Postgres and tests  |
| 1h   | Add configuration using the instance folder and tests |
| 2h   | Review and research websockets                        |
| 0.5h | Tag V0.0.1.0 and documentation                        |

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

1. Create a simple Angular app with Docker (test Dockerfile)
2. Implement the polling service to the REST API of the backend
3. Integrate Grafana and create a simple dashboard with a panel
4. Add a websockets service for real-time data consumption
5. Polish the frontend and add optional features



