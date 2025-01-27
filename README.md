# Introduction

This project demonstrates a full-stack application simulating sensor 
readings from an industrial plant, with a Python backend generating data, 
storing it in a database, and exposing it via an API. A frontend application
will display the data and allow users to interact with it.

## Pre-requisites

To install and run the application, you will need the following software 
installed:

- [Docker](https://docs.docker.com/engine/install/)
- [git](https://git-scm.com/downloads)

## Quick Setup

Create a new directory and navigate to it. Clone the repository using the
following command:

```bash
git clone https://github.com/braboj/sensor-data-app
```

Run the following command to build and start the application:

```bash
docker compose up
```

The following services will be started:

- [Frontend (Angular) / localhost:4200](http://localhost:4200)
- [Backend (Flask) / localhsot:5000](http://localhost:5000)
- [Grafana / localhost:3000](http://localhost:3000)

To access the Grafana dashboard, use the following credentials:

- Username: admin
- Password: admin

## Next Steps
- To leave feedback, please visit [Discussions](https://github.com/braboj/the-great-wall/discussions)
- To contribute, please visit [Contributing](https://github.com/braboj/sensor-data-app/blob/main/CONTRIBUTING.md)