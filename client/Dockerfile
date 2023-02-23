FROM node:14-alpine

WORKDIR /app

COPY ./package*.json ./ 

RUN npm install

COPY . .

# Build the application with
RUN npm run build

# Use a lightweight web server to serve the built application
FROM nginx:alpine

COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

