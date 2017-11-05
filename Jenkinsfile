node {
    
        stage('Build') {
            try {
                println 'Building initially..'
                sh 'python3 sendSuccessMessage.py'
            }
            catch (exc) {
                sh 'python3 sendErrorMessage.py'
            }            
        }
    
        stage('Test') {
            println 'Testing phase..'
            try {
                sh 'python3 hello-world.py'
                sh 'python3 sendSuccessMessage.py'
            }
            catch (exc) {
                sh 'python3 sendErrorMessage.py'
                println 'Failed to run the python script using sh command'
            }            
        }
    
        stage('Deploy') {
            println 'Deploying phase....'
        }
}
