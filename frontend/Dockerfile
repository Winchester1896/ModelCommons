<<<<<<< HEAD
FROM node:16-alpine AS build-stage

#RUN npm install --location=global http-server
#RUN npm install --location=global cors
COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine AS production-stage

COPY --from=build-stage /dist /usr/share/nginx/html

EXPOSE 80

=======
FROM node:16-alpine AS build-stage

#RUN npm install --location=global http-server
#RUN npm install --location=global cors
COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine AS production-stage

COPY --from=build-stage /dist /usr/share/nginx/html

EXPOSE 80

>>>>>>> 174f6ff28139d3a094fb431ff4392023432a03a1
CMD ["nginx", "-g", "daemon off;"]