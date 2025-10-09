const express = require('express');
const router = express.Router();
const pool = require('../db');

// Récupère les prédictions récentes pour un ticker
router.get('/:ticker', async (req, res) => {
  const ticker = req.params.ticker;

  try {
    const assetRes = await pool.query(
      'SELECT id FROM assets WHERE Ticker = $1',
      [ticker]
    );

    if (assetRes.rowCount === 0) {
      return res.status(404).send('Ticker inconnu');
    }

    const assetId = assetRes.rows[0].id;

    const result = await pool.query(
      `SELECT * FROM model_prediction WHERE asset_id = $1 ORDER BY Date DESC LIMIT 50`,
      [assetId]
    );

    res.json(result.rows);
  } catch (err) {
    console.error('Erreur predictions :', err);
    res.status(500).send('Erreur serveur');
  }
});

module.exports = router;