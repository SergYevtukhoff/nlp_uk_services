const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const port = 5002;

// -- api --

app.use(bodyParser.json());
app.listen(port, () => {
    console.log(' * Running on http://0.0.0.0:' + port)
    fs.readFile('/app/data/stopwords_uk.txt', 'utf8', function (err,data) {
        if (err) return console.log(err);
        app.stopwords = data.split('\r\n');
    });
});

app.post('/remove_stopwords', (req, res) => {
	if (!req.body || !req.body.text) return res.sendStatus(400);
    tokens = req.body.text.split(' ').filter((word) => {
        return !app.stopwords.includes(word)
    });
	res.send({
	    text: tokens.join(' ')
	})
});