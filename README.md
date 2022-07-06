# Social Media API

## Description
A RESTful API for a social media app. Built with FastAPI and PostgresQL

Deployed on Heroku: https://social-media-api-jason.herokuapp.com/ and Ubuntu VM: https://www.khaivnguyen02.xyz/

## Usage
1. Clone the repo
2. Install dependencies and packages with `pip install -r requirements.txt`
3. Run `uvicorn app.main:app --reload` to run the server and make the API live
4. Use your browser(with built-in SwaggerUI: add /docs to URL) or Postman to test the REST API.

## Endpoints
**Posts**
- Create a post:     `POST /posts/`
- Get post by ID:    `GET /posts/:id`
- Update a post:     `PUT /posts/:id`
- Delete a post:     `DELETE /posts/:id`

**User**
- Create a user:        `POST /users`
- Get user by ID:       `GET /users/:id`
- Login a user:         `POST /login`

**Vote/Like System**
- Like/Unlike a post:       `POST /vote`
