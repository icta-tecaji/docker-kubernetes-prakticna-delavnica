FROM node:18-alpine

WORKDIR /usr/app

# Install some depenendencies
COPY ./package.json ./
RUN npm install
COPY ./ ./

EXPOSE 8080

# Default command
ENTRYPOINT ["npm", "start"]
