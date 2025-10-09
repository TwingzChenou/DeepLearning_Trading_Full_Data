// backend/routes/assets.js
const express = require('express');
const router = express.Router();
const pool = require('../db');

router.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM assets ORDER BY Ticker');
    res.json(result.rows);
  } catch (err) {
    console.error('Erreur assets :', err);
    res.status(500).send('Erreur serveur');
  }
});

module.exports = router;