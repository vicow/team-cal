# team-cal
=======
A calendar to be shared between team.

## Set up
### Database
Launch MongoDB with:

````
docker run -p 27017:27017 --name team-cal-db --volumes-from dbdata -d mongo --storageEngine wiredTiger
mongo 192.168.99.100:27017
````

**Note:** Find the port with `docker ps` and the IP address with `docker-machine ip default`.

#### Data Persistence
We use a full-container approach. The data is stored in a [data volume container](https://docs.docker.com/engine/userguide/dockervolumes/). Create a new data volume container:

````
docker create -v /dbdata --name dbdata mongo
````

You can now store data using `--volumes-from dbdata` with your `mongo` container. Read about [why it is a good thing](https://medium.com/@ramangupta/why-docker-data-containers-are-good-589b3c6c749e#.oph7e5o92).
