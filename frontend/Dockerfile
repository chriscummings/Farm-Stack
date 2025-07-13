FROM node:24

WORKDIR /code

COPY ./frontend/app/package*.json .

RUN npm install

COPY frontend/app/. .

CMD ["npm", "start"]