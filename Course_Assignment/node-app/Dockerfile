FROM node:14

WORKDIR /web_app

COPY package.json /web_app

RUN npm install

COPY . /web_app

EXPOSE 3000

CMD [ "node" , "server.js" ]

