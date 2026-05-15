pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "ls -la ${WORKSPACE}"
                sh "docker run --rm -u 0:0 -v ${WORKSPACE}:/app -w /app python:3.12 bash -c 'pip install --no-cache-dir -r requirements.txt && python test.py'"
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