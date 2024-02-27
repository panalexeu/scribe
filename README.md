# Scribe

Scribe is an LLM-powered serverless to-do app. Scribe lets users save their tasks and interact with them using LLM.

## Cloud platform

As the cloud platform for `Scribe`, `AWS` was chosen.

## RESTful API implementation

To implement the `Scribe` RESTful API, the framework of choice was:

* `FastAPI` - a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints. It leverages ASGI (Asynchronous Server Gateway Interface) for handling asynchronous requests;

To host the `Scribe` API serverlessly on `AWS`, the package of choice was:

* `Mangum` - an adapter for running ASGI applications in `AWS Lambda` to handle Function URL, API Gateway, ALB, and Lambda@Edge events.

## Database implementation

`Scribe` uses `DocumentDB` provided by `AWS` as the database.

## Architecture

Scribe consists of three microservices:

* Authentication microservice;
* CRUD microservice for tasks in DB handling;
* LLM interaction microservice for communication between the user and LLM.

## LLM implementation

For interactions with `LLM`, `LangChain` was used. As an LLM, the `gpt-3.5-turbo` model was chosen.

## Notes for myself

Packages should be compatible with `AWS Lambda`, installation of the wheel for Linux operating systems and function’s 
instruction set architecture is needed. 

* arm64 package pip installation command: 
    ```
    pip install --platform manylinux2014_aarch64 --target=lambda-packages --implementation cp --python-version 3.10 --only-binary=:all: --upgrade <package_name>
    ```

**Always provide in lambda-packages.zip: packages, app package and .env file!!!**