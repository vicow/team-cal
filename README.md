# team-cal
A calendar to be shared between teams.

## Set up
### Database
Launch MongoDB with:

````
docker run -p 27017:27017 --name team-cal-db --volumes-from dbdata -d mongo --storageEngine wiredTiger
mongo 192.168.99.100:27017
````

**Note:** Find the port with `docker ps` and the IP address with `docker-machine ip default`.

#### Data Persistence
We use a full-container approach. The data is stored in a data-container. Create a new data-container:

````
docker create -v /dbdata --name dbdata mongo
````

You can now store data using `--volumes-from dbdata` with your `mongo` container.
