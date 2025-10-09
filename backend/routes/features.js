const express = require('express');
const router = express.Router();
const pool = require('../db');

// Récupère la dernières features d’un ticker
router.get('/:ticker', async (req, res) => {
  const ticker = req.params.ticker;

  try {
    const result = await pool.query(
      `SELECT * FROM features WHERE Ticker = $1 ORDER BY Date DESC LIMIT 1`,
      [ticker]
    );
    res.json(result.rows);
  } catch (err) {
    console.error('Erreur features :', err);
    res.status(500).send('Erreur serveur');
  }
});

module.exports = router;