pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    # Installer Python dans le conteneur Jenkins
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv git
                '''
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m pytest test.py -v
                '''
            }
        }
    }
}