For Deployment
    1. Git clone to aws
    2. Set Environment:- python3 -m vnev flaskenv
    3. Activate environment:- source flaskenv/bin/activate
    4. pip3 install -r requirements.txt
    5. flask db init    flask db migrate   flask db upgrade
    5. Run Server:- flask run --host=0.0.0.0 --port=5000
    6. Run Gunicorn:- gunicorn --bind=0.0.0.0:5000 app:app
    7. nohup :- 
