# team-cal
A calendar to be shared between teams.

## Set up
### Database
Launch MongoDB with:

````
docker run -p 27017:27017 --name team-cal-db -d mongo
mongo 192.168.99.100:27017
````

**Note:** Find the port with `docker ps` and the IP address with `docker-machine ip default`.
