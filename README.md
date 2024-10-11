# Rick and Morty Docker example 

### Project Overview
This repository serves as a practice project for learning and exploring **Docker** and **Docker Compose.** I set out to learn how to containerize applications, manage multi-container setups, and orchestrate communication between services using Docker Compose.

## The project includes:

An API container that fetches data from an external API and stores it in a shared Docker volume.
A Plotting container that reads the data from the shared volume and generates visualizations, saving them locally.
This setup showcases the fundamentals of Docker, container management, and inter-container communication.


## How to Run the Project

1. **Clone the Repository**:
```bash
git clone https://github.com/dmorton714/rick_morty_docker.git
cd rick_morty_docker
```

2. Build and Start the Containers: Make sure Docker and Docker Compose are installed on your machine. Then, run:

```bash
docker-compose up --build
```

3. Check the Output:
- The API container will fetch the data from the API (or load it from a cached CSV file).
- The Plot container will read the data and generate a plot, saving it in the data folder.
- View the Plot: The plot will be saved in the data/ directory. You can view it from the local directory after the containers have run.

4. Stop the Containers: To stop the containers, press Ctrl + C in the terminal where docker-compose is running, or use:

``` bash
docker-compose down
```