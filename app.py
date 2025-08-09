import logging
from __init__ import create_app, db

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = create_app()

with app.app_context():
    # Create tables
    db.create_all()
    
    # Initialize data
    from init_data import init_courses
    init_courses()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
