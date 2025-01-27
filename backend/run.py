import os

from app import create_app
from flask_cors import CORS

app = create_app(
    {
        'SQLALCHEMY_DATABASE_URI': os.getenv("DATABASE_URL", "sqlite:///test.db"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }
)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)