pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/pkjkumar66/my-app.git'
        BUILD_DIR = 'build'
        DOCKERHUB_USERNAME = pkjkumar66
        DOCKERHUB_PASSWORD = V@rLhdfztFTj459
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the source code from your Git repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], userRemoteConfigs: [[url: env.GITHUB_REPO]]])
            }
        }

        stage('Set Up Environment') {
            steps {
                tool name: 'Python3.9', type: 'hudson.plugins.python.PythonInstallation'

                 // Install project dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                 // Perform the necessary build steps (if any)
                sh 'python build.py'
            }
        }

        stage('Test') {
            steps {
                // Run tests for your Python application
                sh 'python -m unittest discover'
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build and tag the Docker image
                    def imageName = "pkjkumar66/my-app:${BUILD_NUMBER}" // Tag the image with the Jenkins build number
                    sh "docker build -t ${imageName} ."

                    // Log in to DockerHub using credentials
                    sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"

                    // Push the Docker image to DockerHub
                    sh "docker push ${imageName}"
                }
            }
        }
    }
}
