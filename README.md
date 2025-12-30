# Software Design Principles

This project aims to cover good examples reflecting the purpose and usage of Software Design Principles and common patterns.

---

## 🚀 Getting Started

These instructions will get a copy of the project up and running on your local machine using Docker.

### Prerequisites

You need to have the following installed:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
* [Git](https://git-scm.com/)

### 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone git clone git@github.com:coder-richa/software-design-principles.git
   cd software-design-principles
   ```

2. **Build the Docker Image**
 This command creates an image named software-design-principles based on the Dockerfile.

    ```bash
    docker build -t software-design-principles .
    ```
3. **Run the Container Execute the application within the isolated container.**
    
    ```bash
    docker run --name running-app software-design-principles
    ```
### 📦 Usage 
Development Mode (Hot Reloading)
To edit your code and see changes immediately without rebuilding the image, use a volume mount to sync your local app/ folder with the container:

```bash

docker run -v $(pwd)/app:/app software-design-principles
```
### Accessing the Shell
If you need to inspect the environment or run manual commands inside the container:

```bash
docker run -it software-design-principles /bin/bash
```
### 🔧 Maintenance
Adding Dependencies
Open requirements.txt and add the required package.

Rebuild the image to install the new layers:

```bash
docker build -t software-design-principles .
```
### Cleaning Up
To remove the container and the image when finished:

```bash
docker rm running-app
docker rmi software-design-principles
```
