
FROM node:17-alpine

RUN npm install -g nodemon

WORKDIR /flash-service-info-to-card

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3003

CMD ["npx", "nodemon", "index.js"]
