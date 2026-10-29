pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage 1: Checkout source code from repository'
            }
        }

        stage('Pytest Execution') {
            steps {
                echo 'Stage 2: Running Pytest and printing test case...'
                bat 'pytest -v -s'
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
                bat 'python monitor.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed successfully.'
        }
    }
}
