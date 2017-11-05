pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building initially..'

                System.properties['os.name']
                if (System.properties['os.name'].toLowerCase().contains('windows')) {
                    println "it's Windows"
                } 
                else {
                    println "it's not Windows"
                }

                echo 'python3 hello-world.py'
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
