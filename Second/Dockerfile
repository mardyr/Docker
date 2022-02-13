FROM node

WORKDIR /app

#copy file with notes about dependecies on the basis of which enviroment will be prepared 
COPY package.json /app

# prepare environment
RUN npm install 

#copy code
COPY . /app

#map port 80 from a container to local machine, like open a pipe on port 80 inside a container
# -p (publish) flag is obligatory to access container from local host
#syntax -p (local_port) (container_port - here is 80)
EXPOSE 80

#command will be run during starting a contatiner, not an image
#container layer
CMD [ "node" , "server_first.js" ]
