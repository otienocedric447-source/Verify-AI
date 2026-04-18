from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from your_blueprint_file import auth_bp, detect_bp, user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(detect_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)