# nlp_uk_services
Here is a bunch of microservices for typical (ukrainian) text processing tasks, including removing punctuation and stopwords, lemmatization.

Following microservices have been implemented:
1. /pr - basic text preprocessing which includes removing unwanted characters (like ¬_}|{±¶•§®™ ), replacing multiple forms of dashes and apostrophes for one "canonical" form
2. /sw - removes stopwords
3. /lm - does lemmatization for each word of input text

## Using
### Prerequisites
docker engine, docker composer

### Running
1. Clone the repo
2. ``docker-composer build``
3. ``docker-composer up``

### API
|Service name|URL|cURL example|
|------------|---|------|
|pr|``http://[pr_host]:[pr_port]/process``|curl -X POST -d '{"text": "приклад тексту"}' [pr_host]:[pr_port]/process|
|sw|``http://[sw_host]:[sw_port]/remove_stopwords``|curl -X POST -d '{"text": "приклад тексту"}' [sw_host]:[sw_port]/remove_stopwords|
|lm|``http://[lm_host]:[lm_port]/lemmatize``|curl -X POST -d '{"text": "приклад тексту"}' [lm_host]:[lm_port]/lemmatize|

### Example
Here is also a microservice **nlp_test**, that makes api-calls to each of services above and returns a processed, lemmatized text.

**Request:**</br>
curl -X POST -d '{"text": "\"З понеділка в Україні - літо. Практично у всіх областях буде сухо, дуже тепло і сонячно жарко. Температура повітря буде розкручуватися від + 22 + 28 до + 26 + 32 градусів\""}' [nlp_test_host]:[nlp_test_port]/process

**Response:**</br>
{"text": "понеділок україна - літо практично область сухо тепло сонячно жарко температура повітря розкручуватися градус"}
