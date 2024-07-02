FROM python:3.9

ENV APP_CODE="/application"
WORKDIR ${APP_CODE}
COPY . .

RUN pip install -r requirements.txt

# Expose the port where the Flask app runs
EXPOSE 5000

# Run the gunicorn server for your Flask app
CMD ["python", "app.py"]