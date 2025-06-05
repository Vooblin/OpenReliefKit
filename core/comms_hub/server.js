const express = require('express');
const http = require('http');
const { Server } = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new Server({ server });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    ws.send(`echo: ${message}`);
  });
});

app.get('/', (req, res) => {
  res.send('Comms Hub');
});

server.listen(3001, () => {
  console.log('Comms Hub listening on port 3001');
});
