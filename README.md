# Social Media API

## Description
A RESTful API for a social media app. Built with FastAPI and PostgresQL

## Usage
1.Clone the repo
2. Install dependencies and packages with `pip install -r requirements.txt`
4. Run `uvicorn app.main:app --reload` to run the server and make the API live
5. Use your browser or Postman to test the REST API.

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
