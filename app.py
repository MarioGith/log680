from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from api.routes import register_routes

app = Flask(__name__)
api = Api(app)

# Initialize Swagger
swagger = Swagger(app)

# Register routes
register_routes(api)

if __name__ == '__main__':
    app.run(debug=True)