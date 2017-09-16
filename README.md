# Flask-Exemplar

## Contributors
* [Larry Hignight](https://github.com/Larry-Hignight/)
* [George Vamos](https://github.com/gvamos)
* [Mike Finley](https://github.com/michael-finley)


## Example Usage

Issue the following commands to build and run the container:

* sudo docker build --rm -t flask .
* sudo docker run -p 80:5000 flask

The hello world application will be available on port 80 of the host machine.

* sudo docker network inspect bridge

Used to inspect the network settings.


## AWS Checklist

* Change the Security Groups setting for the current EC2 instance to allow inbound connections
* Clone the following Github repos: Linux-Scripts and Flask-Exemplar
* Run the Linux-Scripts/github-setup.sh script
* Run the Linux-Scripts/Docker/docker-ce-install-ubuntu.sh script
* Build and run the Docker container from the Flask-Examplar directory


## TO DO

* Clean up the pip install portion of the Dockerfile
* Incorporate additional functionality from Miguel's blog/book and PyCon 2016 talk.
* Create a compose file
* Push image to Dockerhub
* Add the following return types to the view:  JSON, XML, PNG and JPEG.

