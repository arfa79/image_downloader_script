# Image Processing Script

This script is designed to download images from Google search results, perform resizing tasks, and store the processed images in a PostgreSQL database. It emphasizes asynchronous programming techniques for optimal efficiency.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Local Development](#local-development)
  - [Docker](#docker)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Create a versatile script capable of downloading images from Google search results based on a specified search query string, such as "cute kittens." Perform resizing tasks on the downloaded images and securely store them in a PostgreSQL database. This script offers flexibility by supporting multiple programming languages, including Node.js, Go, Java, .NET, and Python, allowing you to choose the language you're most comfortable with. When using the script, provide inputs for the search query, the maximum number of images to be fetched, and essential PostgreSQL database connection details. The script's design emphasizes asynchronous programming techniques to optimize efficiency, and it comes equipped with a suite of unit tests to ensure reliability and robustness. Additionally, consider Docker containers for convenient project encapsulation and deployment.

---

## Features

- Versatile image downloading from Google search results
- Asynchronous image processing and resizing
- Secure storage of resized images in a PostgreSQL database
- Language flexibility with support for multiple programming languages
- User-configurable input for search query and maximum number of images
- Design emphasizes asynchronous programming techniques for efficiency
- Docker container support for project encapsulation and deployment

---

## Prerequisites

- Python 3.9
- Docker 

---

## Getting Started

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arfa79/image_processing_script.git
   cd image_processing_script

2. **install dependencies:**

    ```bash
    pip install -r requirements.txt

3. ***Run the script:***

    ```bash
    python your_script.py

4. ***Docker:***

    Build the Docker image:

    ```bash
    docker build -t image-processing-script .

5. ***Run the Docker container:***

    ```bash
    docker run -it --rm image-processing-script

## Usage

Update the url_query_list in script.py with your desired image URLs and queries.
Run the script as per the Getting Started instructions.

## Configuration

Adjust the configurations in script.py based on your requirements:

    Database connection details (CONFIG['db']).
    Google API key (CONFIG['google_api_key']).
    Image resize dimensions (CONFIG['image_resize_dimensions']).
    Output directory for resized images (CONFIG['output_resized_images']).

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the GNU3 License.
