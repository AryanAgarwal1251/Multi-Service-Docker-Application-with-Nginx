# Multi-Service-Docker-Application-with-Nginx
#### A Python based web application that uses Streamlit for frontend and provides a dataset analysis service, a sentiment predictor using VADER lexicon and SQLite-3 powered logging service. The application uses Nginx for load balancing and reverse proxy for efficient traffic management  across the services.

### P.S.: I am currently working on hosting this project online! For now, please use the instructions given below to access the project and web application using the given below instructions.

### Instructions to Download:
- git clone https://github.com/AryanAgarwal1251/Multi-Service-Docker-Application-with-Nginx.git
- cd Multi-Service-Docker-Application-with-Nginx
- docker-compose up --build

### Here are the links:
- For accessing the web application: http://localhost:8080
- For frontend (Streamlit): http://localhost:8501
- Logging Service: http://localhost:6000/logs
- ML Service (Flask): http://localhost:5000/predict
- Analysis Service (Flask): http://localhost:5050/analyze

### To stop the application:
- docker-compose down

SCREENSHOTS:

<img width="1919" height="1065" alt="image" src="https://github.com/user-attachments/assets/d7153ba6-e582-4d31-a522-bf78082dd6cf" />





Using the testcase: "My new phone's camera is amazing, but the battery life is completely useless."

<img width="1915" height="1065" alt="image" src="https://github.com/user-attachments/assets/de43da40-9d8e-4d13-9d03-6f6c037f77b1" />





Uaing the testcase: "The service at the new cafe was an absolute disaster, but the coffee was surprisingly excellent."

<img width="1919" height="1065" alt="image" src="https://github.com/user-attachments/assets/1e077809-3ef6-4e44-b03e-260be42c233f" />





Uploading a dataset:

For my illustration, I am using the Uber Analytics Dashboard dataset (Link: https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard)



<img width="1919" height="999" alt="image" src="https://github.com/user-attachments/assets/db467735-5f25-4497-9202-d7fa30fa4296" />




Output:



<img width="1919" height="1067" alt="image" src="https://github.com/user-attachments/assets/3a8759a1-011a-423e-81ed-be9ccaa9c2f0" />





Fetching Logs:



<img width="1919" height="1057" alt="image" src="https://github.com/user-attachments/assets/0c061892-2f28-4433-ac83-b3ea845a64d7" />





ARCHITECTURE:


<img width="455" height="652" alt="image" src="https://github.com/user-attachments/assets/e1d326a0-f57f-44c9-9de8-71ffbe3199a2" />


REPOSITORY STRUCTURE:


my-multiservice-app/
├── frontend/        # React/Vue/Angular frontend
├── backend/         # Python backend with SQLite
├── nginx/           # Nginx reverse proxy configuration
├── docker-compose.yml
└── README.md


## Features

- **Multi-Service Architecture**: Independent containers for Frontend, ML Service, Analysis Service, and Logging Service, promoting modularity and easier maintenance.
- **Machine Learning Integration**: Real-time sentiment analysis using a trained ML model deployed inside its own container.
- **Dataset Analysis**: Upload a ZIP dataset containing CSV files and generate correlation heatmaps for quick insights.
- **Centralized Logging**: All services send logs to a Logging Service backed by SQLite3 for persistent storage and easy retrieval.
- **User-Friendly Frontend**: Streamlit interface for submitting reviews, uploading datasets, and viewing logs.
- **NGINX Reverse Proxy & Load Balancer**: Routes traffic, balances load across replicas, and provides a single entry point for the application.
- **Dockerized Deployment**: Each service runs in its own container; `docker-compose` manages orchestration, scaling, and networking.
- **Backup Containers (Warm Standby)**: Backup services for failover and high availability.
- **Scalability with Replicas**: Multiple replicas for frontend, ML, and analysis services to improve fault tolerance and performance.
- **Live Code Reloading**: Optional development mode with mounted volumes for instant code updates inside containers.



- **Frontend**: Streamlit app for user interaction.
- **ML Service**: Processes user input and predicts sentiment.
- **Analysis Service**: Processes uploaded datasets and generates visualizations.
- **Logging Service**: Collects logs from all services in SQLite3.
- **NGINX**: Provides a single entry point and balances requests across service replicas.

---

## Technologies Used

- **Programming & Frameworks**: Python, Flask, Streamlit, Pandas, Matplotlib, Seaborn
- **Machine Learning**: Vader Sentiment Analyzer
- **Databases**: SQLite3
- **Containerization & Orchestration**: Docker, Docker Compose
- **Web Server & Load Balancer**: NGINX
- **Version Control & Hosting**: GitHub

---

## Project Highlights

- Fully Dockerized multi-service application.
- ML-powered sentiment analysis with independent service container.
- Dataset analysis service that generates heatmaps for insights.
- Centralized logging using SQLite3 database.
- Scalable deployment with multiple replicas and warm standby backup services.
- NGINX reverse proxy ensures single entry point and load balancing.
- Easy to run locally with minimal setup using `docker-compose`.

---

## Future Improvements

- Extend ML capabilities with more models (e.g., multi-class classification, NLP pipelines).
- Add authentication and user management.
- Implement persistent storage for dataset uploads.
- Integrate more interactive visualizations for dataset analysis.
- Deploy to cloud platforms (AWS/GCP/Azure) for production-level scalability.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## My Information
- Name: Aryan Agarwal
- Student at Vellore Institute of Chennai, India
- Email: aryanagarwal0125@gmail.com
