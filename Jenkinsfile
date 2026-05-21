pipeline {
    agent {
        kubernetes {
            label 'jenkins-agent-flask'
            yaml """
                apiVersion: v1
                kind: Pod
                metadata:
                    labels:
                        component: ci
                spec:
                    containers:
                    - name: python
                        image: python:3.11
                        command: ['cat']
                        tty: true
                    - name: docker
                        image: docker:latest
                        command: ['cat']
                        tty: true
                        volumeMounts:
                        - mountPath: /var/run/docker.sock
                          name: docker-sock
                    - name: kubectl
                        image: lachlanevenson/k8s-kubectl:v1.17.2
                        command: ['cat']
                        tty: true
                    volumes:
                    - name: docker-sock
                        hostPath:
                          path: /var/run/docker.sock
            """
        }
    }

    environment {
        // !!! REMPLACE PAR TON PSEUDO DOCKER HUB !!!
        DOCKER_USER = 'mandrindraesperant'
        IMAGE_NAME = "flask-hello"
        DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Test python') {
            steps {
                container('python') {
                    sh "pip install -r requirements.txt"
                    sh "python test.py"
                }
            }
        }

        stage('Build & Push Image') {
            steps {
                container('docker') {
                    sh "docker login -u ${DOCKER_HUB_CREDS_USR} -p ${DOCKER_HUB_CREDS_PSW}"
                    sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:latest ."
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                container('kubectl') {
                    sh "kubectl apply -f ./kubernetes/deployment.yaml"
                    sh "kubectl apply -f ./kubernetes/service.yaml"
                    sh "kubectl rollout restart deployment/pythontest"
                }
            }
        }
    }
}