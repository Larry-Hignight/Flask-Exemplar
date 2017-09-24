# Flask-Exemplar

## Contributors
* [Larry Hignight](https://github.com/Larry-Hignight/)
* [George Vamos](https://github.com/gvamos)
* [Mike Finley](https://github.com/michael-finley)


## Example Docker Usage

Issue the following commands to build and run the container:

* docker build --rm -t flask .                             # Builds an image named flask
* docker run -p 80:5000 flask                              # Container will be running on port 80
* docker network inspect bridge                            # Inspect the network settings


## Example Docker Swarm Usage

* docker stack deploy -c <compose-file> flask_swarm      # Deploys a swarm named flask_swarm
* docker container ls                                      # List the running containers
* docker stack rm flask_swarm                              # Stops the swarm named flask_swarm
* docker swarm init                                        # If you get the "this node is not a swarm manager"
* ...                                                      # error when deploying the stack then issue this cmd


## Example Multi-Node Swarm Setup

* docker swarm init --advertise-addr <ip-addr>             # Init the swarm manager and copy the join info
* docker swarm join --token <token> <mngr-ip-addr:port>    # Adds worker node to the swarm managed above
* docker node ls                                           # List all nodes in the current swarm
* docker stack ps <swarm-name>                             # List all containers in the swarm (across all nodes)


## AWS Checklist

* Change the Security Groups setting for the current EC2 instance to allow inbound connections
* Clone the following Github repos: Linux-Scripts and Flask-Exemplar
* Run the Linux-Scripts/github-setup.sh script
* Run the Linux-Scripts/Docker/docker-ce-install-ubuntu.sh script
* Build and run the Docker container from the Flask-Examplar directory


## RDBMS Notes

* docker exec -it <container> mysql -uroot -p     # Execute mysql client w/ a MySQL container
* docker exec -it <container> psql -U postgres    # Execute psql client w/ a Postgres container


## Change Log

### Docker Related
* DONE - Add compose file for MySQL
* DONE - Add compose file for Postgres
* TODO - Missing log output when run using "docker stack deploy"
* TODO - Push image to Docker Hub
* TODO - Clean up the pip install portion of the Dockerfile

### Flask Related
* TODO - Incorporate additional functionality from Miguel's blog/book and PyCon 2016 talk.
* TODO - The Flask-WTF and OpenID stuff in Chap 3 is dated and needs to be replaced.
* TODO - Add the following return types to the view:  JSON, XML, PNG and JPEG.

### Misc
* TODO - Create Behave scripts to populate the database and test the application stack
* TODO - Create separate exemplars for the databases
* TODO - Create NoSQL compose files
