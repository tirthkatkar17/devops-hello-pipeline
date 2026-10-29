pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage 1: Checkout source code from repository'
                checkout scm
            }
        }

        stage('Pytest Execution') {
            steps {
                echo 'Stage 2: Installing requirements and running Pytest...'
                bat 'python -m pip install --upgrade pip pytest'
                bat 'python -m pytest -v -s'
            }
        }

        stage('Docker Build & Run') {
            steps {
                echo 'Stage 3: Building lightweight Python Docker image...'
                bat 'docker build -t hello-python:latest .'
                echo 'Stage 4: Running Docker container with Hello.py...'
                bat 'docker run --rm hello-python:latest'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                echo 'Stage 5: Running Evidently tool and generating monitoring report...'
                // Added a timeout so it fails gracefully instead of hanging for 10+ minutes
                timeout(time: 3, unit: 'MINUTES') {
                    bat 'python -m pip install evidently'
                    bat 'python monitor.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}