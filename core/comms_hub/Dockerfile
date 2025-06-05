FROM node:20-alpine
WORKDIR /app
COPY package.json package.json
RUN npm install --production
COPY server.js server.js
CMD ["node", "server.js"]
