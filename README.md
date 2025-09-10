# Multi-Service-Docker-Application-with-Nginx
A Python based web application that uses Streamlit for frontend and provides a dataset analysis service, a sentiment predictor using VADER lexicon and SQLite-3 powered logging service. The application uses Nginx for load balancing and reverse proxy for efficient traffic management  across the services.

P.S.: I am currently working on hosting this project online! For now, please use the instructions given below to access the project and web application using the given below instructions:

git clone https://github.com/AryanAgarwal1251/Multi-Service-Docker-Application-with-Nginx.git
cd Multi-Service-Docker-Application-with-Nginx
docker-compose up --build

Now, you can access the application!
Here are the links:
For accessing the web application: http://localhost:8080
For frontend (Streamlit): http://localhost:8501
Logging Service: http://localhost:6000/logs
ML Service (Flask): http://localhost:5000/predict
Analysis Service (Flask): http://localhost:5050/analyze

To stop the application:

docker-compose down

SCREENSHOTS:

<img width="1919" height="1065" alt="image" src="https://github.com/user-attachments/assets/d7153ba6-e582-4d31-a522-bf78082dd6cf" />

<img width="1915" height="1065" alt="image" src="https://github.com/user-attachments/assets/de43da40-9d8e-4d13-9d03-6f6c037f77b1" />

