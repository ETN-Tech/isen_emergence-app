/**
 * API ACCOUNTS ROUTER
 * Handle all /api/accounts requests
 */

const accounts = require('express').Router();

const accountsController = require('../../controllers/accounts');

// GET routes
accounts.get('/', accountsController.list);
accounts.get('/:id([0-9]+)', accountsController.getById);
accounts.get('/:token([0-9a-z]{128})', accountsController.getByAccessToken);
accounts.get('/laureates', accountsController.listLaureates);
accounts.get('/godfathers', accountsController.listGodfathers);

// POST routes
accounts.post('/', accountsController.insert);

// PUT routes
accounts.put('/:id([0-9]+)', accountsController.update);

// DELETE routes
accounts.delete('/:id([0-9]+)', accountsController.delete);

module.exports = accounts;
