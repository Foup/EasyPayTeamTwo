pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('example build') {
            steps {
                sh 'bash python --version'
            }
        }
    }
}