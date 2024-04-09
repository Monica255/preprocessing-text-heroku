# Preprocessing Flask API

This repository contains a simple Flask API for text preprocessing. The API utilizes the Sastrawi library for stemming and is deployed on Heroku.

## Usage

### Base URL
The base URL for the API is: [https://flask-heroku3-8ee949830100.herokuapp.com/](https://flask-heroku3-8ee949830100.herokuapp.com/)

### Endpoint
The endpoint for preprocessing text is:

```
GET /api
```

### Request Body
The request body should be in JSON format and include the text to be preprocessed. For example:

```json
{
    "text": "Bagaimana cara memanen jagung"
}
```

### Response
The API will respond with the preprocessed text.

## Example

### Request
```http
GET /api
Content-Type: application/json

{
    "text": "Bagaimana cara memanen jagung"
}
```

### Response
```json
{
    "data": "cara panen jagung"
}
```

## Deployment

This API is deployed on Heroku. You can access it via the base URL provided above.

## Dependencies
- Flask
- Sastrawi

## Local Setup
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python main.py`.
4. The API should now be running locally.

## Credits
- Sastrawi Library: [https://github.com/sastrawi/sastrawi](https://github.com/sastrawi/sastrawi)

Feel free to fork and modify this repository for your own use! If you have any questions or issues, please don't hesitate to contact me.
