# Introduction

This project is designed to showcase a full-stack project that simulates
sensor readings from an industrial plant, stores them in a database and offers
a front-end to visualize the sensor readings.

## Installation

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