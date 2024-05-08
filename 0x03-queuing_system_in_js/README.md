# Queueing systems in Javascript

In this project, we explore creting queueing systems in the backend to help us carry out tasks that
we can offload to other services and not the API e.g sending bulk emails, processing jobs or caching server data.

In this example we use Redis to create:
1. Publisher/Subscriber pattern.
2. Job processing with queues.
3. Seat reservation system logic to prevent booking over the maximum amount / ensure transactions do not collide.
4. Stock keeping API logic.

## Requirements

1. Redis
2. Vagrant
3. NodeJS
4. Kue
5. ExpressJS

## Installation

You can use `vagrant` to create a virtual machine with the required packages. Run the vagrant file found in the root of the repo then install `nvm` to cap `nodejs` at version `12` to work with `node-redis`.

## Run the project

Run the server on the desired file associated with the task.
Ensure the redis server is runnning.

```sh
npm run dev <file_name>
```
