## For Deployment
* 1. Git clone to aws
* 2. Set Environment:- python3 -m vnev flaskenv / python -m virtualenv flask
* 3. Activate environment:- source flaskenv/bin/activate
* 4. pip3 install -r requirements.txt
* 5. flask db init    flask db migrate   flask db upgrade
* 6. Run Server:- flask run --host=0.0.0.0 --port=5000
* 7. Run Gunicorn:- gunicorn --bind=0.0.0.0:5000 app:app
  8. Run gunicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:5000 app:app
* 8. nohup :- 
* 9. Run XVFB for screen:- Xvfb :99 -screen 0 1024x768x16 &
* 10. export DISPLAY=:99



