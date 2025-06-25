# arionkoder-custom-iterator-lazy-evaluation
This repository contains the implementation for the 'Custom Iterator with Lazy Evaluation' exercise.

# Usage Options
After cloning the project using the command `git clone https://github.com/BastosDiogo/arionkoder-custom-iterator-lazy-evaluation.git`,  choose one of the two options below to run the project:

1-) Fully containerized application:

• Build the container image with the following command: `sudo docker build -t iterator-lazy .`

• Then, create and run the container with the following command: `sudo docker run -p 8000:8000 iterator-lazy`

• Then in a browser set `http://localhost:8000/docs`

2-) Running locally:

• Create a Python virtual environment using the appropriate command for your OS (Linux or Windows) and activate it.

• Then install Poetry with `pip install poetry`, and navigate to the `app` directory and run `poetry install`;

• While still in the `app` directory, run: `uvicorn main:app --reload`. Then in a browser set `http://127.0.0.1:8000/docs`

# Running the application

• The Lazy Iterator is running behind the scenes for all endpoints accessible via `http://localhost:8000/docs` or `http://127.0.0.1:8000/docs` (depending on how you've set up the project). 

• Simply use the available endpoints as needed and observe their responses.
