# my-app

## Description

This project is a simple to-do app that allows users to manage their tasks. Users can add new tasks, view their existing tasks, and delete tasks when they are completed. The app provides a straightforward interface for organizing and tracking your to-do list.


## Postman Collection

Explore and test the APIs using the provided Postman collection.

[Postman Collection](https://red-water-686645.postman.co/workspace/My-Workspace~bfb5c795-ecc4-4e23-8ad9-7c7fe4b847b4/collection/25669291-4880319b-c547-4a21-b231-07fbed39937f?action=share&creator=25669291)

## Docker Image

Pull the Docker image from DockerHub:

```bash
docker pull pkjkumar66/my-app:latest
```


## APIs

### Home Page

Get the home page.

```bash
curl --location 'http://127.0.0.1:5000/'
```

### Add Items
Add a new task to the to-do list.
```bash
curl --location 'http://127.0.0.1:5000/add_item' \
--header 'Content-Type: application/json' \
--data-raw '{ "username" : "Pankaj", "item" : "take devops session" }'
```

### View Item
View the to-do list for a specific user.
```bash
curl --location 'http://127.0.0.1:5000/view_items/Pankaj'
```


### Delete Items
Delete a task from the to-do list for a specific user by item ID.
```bash
curl --location --request DELETE 'http://127.0.0.1:5000/delete_item/Pankaj/3'
```



## Docker Container
Run the app on your local machine using a Docker container:
```bash
docker run -p 5000:5000 pkjkumar66/my-app:latest
```

## Installation
- Clone the repository.
- Install the required dependencies.
- Run the application.


## Usage
- Access the home page to get started.
- Add tasks to your to-do list using the "Add Items" API.
- View your current tasks using the "View Item" API.
- Delete completed tasks using the "Delete Items" API.


## Contributing
We welcome contributions! Please follow our guidelines for contributing to this project.
