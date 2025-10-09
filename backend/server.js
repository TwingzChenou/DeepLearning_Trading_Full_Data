
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Route de test
app.get('/', (req, res) => {
  res.send('✅ Backend en ligne');
});

// Lancer le serveur sur 0.0.0.0 pour Docker
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Serveur lancé sur http://localhost:${PORT}`);
});