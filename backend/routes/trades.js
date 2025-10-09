const express = require('express');
const router = express.Router();
const pool = require('../db');

// Récupère les 100 derniers trades d’un ticker
router.get('/:ticker', async (req, res) => {
  const ticker = req.params.ticker;

  try {
    const result = await pool.query(
      `SELECT * FROM trades WHERE Ticker = $1 ORDER BY Date DESC LIMIT 100`,
      [ticker]
    );
    res.json(result.rows);
  } catch (err) {
    console.error('Erreur trades :', err);
    res.status(500).send('Erreur serveur');
  }
});

module.exports = router;
