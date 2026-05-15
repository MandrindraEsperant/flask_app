pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "pip install -r requirements.txt"
                sh "python test.py"
            }
        }
        stage('Build image') {
            steps {
                sh "docker build -t mandrindraesperant/flask-hello ."
            }
        }
        stage('Push image') {
            steps {
                sh "docker push mandrindraesperant/flask-hello"
            }
        }
    }
}