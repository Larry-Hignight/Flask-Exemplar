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


## TO DO

* Clean up the pip install portion of the Dockerfile
* Incorporate additional functionality from Miguel's blog/book and PyCon 2016 talk.
* Create a compose file
* Add the image to Dockerhub
