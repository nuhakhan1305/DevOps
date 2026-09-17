pipeline {
    agent any

    environment {
        PATH = "/Users/nuhakhan/.docker/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Check Docker') {
            steps {
                sh 'which docker'
                sh 'docker --version'
            }
        }

        stage('Build') {
            steps {
                echo "Build Docker Image"
                sh "docker build -t mypythonflaskapp ."
            }
        }

        stage('Run') {
            steps {
                echo "Run application in Docker Container"

                sh "docker rm -f mycontainer || true"

                sh "docker run -d -p 5002:5002 --name mycontainer mypythonflaskapp"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}