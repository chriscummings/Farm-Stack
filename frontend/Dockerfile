FROM node

WORKDIR /code

COPY ./frontend/app/package*.json .

RUN npm install

COPY frontend/app/. .

CMD ["npm", "start"]