# Scribe

Scribe is an LLM-powered serverless to-do app. Scribe lets users save their tasks and interact with them using LLM.

## Cloud platform

As the cloud platform for `Scribe`, `AWS` was chosen.

## RESTful API implementation

To implement the `Scribe` RESTful API, the framework of choice was:

* `FastAPI` - a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints. It leverages ASGI (Asynchronous Server Gateway Interface) for handling asynchronous requests;

To host the `Scribe` API serverlessly on `AWS`, the package of choice was:

* `Mangum` - an adapter for running ASGI applications in AWS Lambda to handle Function URL, API Gateway, ALB, and Lambda@Edge events.

## Database implementation

`Scribe` uses `DocumentDB` provided by `AWS` as the database.

## Architecture

Scribe consists of three microservices:

* Authentication microservice;
* CRUD microservice for tasks in DB handling;
* LLM interaction microservice for communication between the user and LLM.

## LLM implementation

For interactions with `LLM`, `LangChain` was used. As an LLM, the `gpt-3.5-turbo` model was chosen.
