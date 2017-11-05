pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building initially..'
                sh 'python3 hello-world.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing phase..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying phase....'
            }
        }
    }
}
