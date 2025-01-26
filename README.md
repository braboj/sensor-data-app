# Introduction

This project demonstrates a full-stack application simulating sensor 
readings from an industrial plant, with a Python backend generating data, 
storing it in PostgreSQL, and exposing it via an API. 

The Angular frontend visualizes the data in real-time, enabling users to 
customize dashboards using frameworks like Grafana. Seamless integration, 
testing, and deployment are ensured through Docker, with optional features 
like user authentication and dashboard persistence.

## Quick Setup

To get started, you will need to install Docker. You can find the installation
instructions on this page:

- [Install Docker Engine](https://docs.docker.com/engine/install/).

After that, you can run the following command to get the project image:

```bash
docker pull braboj/wall_project:latest
```

And finally, you can run the following command to start the project:

```bash
docker compose up
```

To access the front-end, open your browser and navigate to:

- [http://localhost:4200](http://localhost:4200)

To access the back-end, open your browser and navigate to:

- [http://localhost:5000](http://localhost:5000)

The Grafana service is accessible using the following link:

- [http://localhost:3000](http://localhost:3000)

The username and password are both `admin`.

## Next Steps
- To leave feedback, please visit [Discussions](https://github.com/braboj/the-great-wall/discussions)
- To contribute, please visit [Contributing](https://github.com/braboj/sensor-data-app/blob/main/CONTRIBUTING.md)