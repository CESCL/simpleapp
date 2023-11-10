pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/CESCL/simpleapp.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile main.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest'
            }
        }
    }
}