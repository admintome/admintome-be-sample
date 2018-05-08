# Sample Application Backend

This repository is part of a sample application.  It provides the back-end of the application that exposes API endpoints for manageing books.  It also makes use of a MongoDB containerfor the storage.

## Docker commands

The following commands will build and run the application backend

```
docker build -t admintome-sample .
docker run --name mongo -d mongo
docker run --link mongo:mongo -p 8888:8888 --name admintome-sample admintome-sample
```

## API Endpoints

### Get all books

```
GET http://localhost:8888/v1/getbooks
```

### Add a book

```
POST http://localhost:8888/v1/addbook?title="{title}"&author="{author}"
```

### Delete a book

```
GET http://localhost:8888/v1/delbook?id="id"
```
