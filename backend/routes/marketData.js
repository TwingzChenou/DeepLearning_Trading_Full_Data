// backend/routes/marketData.js
const express = require('express');
const router = express.Router();
const pool = require('../db');

router.get('/:ticker', async (req, res) => {
  const ticker = req.params.ticker;

  try {
    const result = await pool.query(
      'SELECT * FROM market_data WHERE Ticker = $1 ORDER BY Date DESC LIMIT 100',
      [ticker]
    );
    res.json(result.rows);
  } catch (err) {
    console.error('Erreur market_data :', err);
    res.status(500).send('Erreur serveur');
  }
});

module.exports = router;