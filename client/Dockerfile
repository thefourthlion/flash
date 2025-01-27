FROM node:18-alpine

WORKDIR /flash-client

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3001

ENV PORT 3001
ENV NODE_ENV production
ENV HOSTNAME "0.0.0.0"

CMD ["npm", "start"]