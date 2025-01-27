
FROM node:17-alpine

RUN npm install -g nodemon

WORKDIR /flash-server

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3002

CMD ["npx", "nodemon", "index.js"]
