node {
    
        stage('Build') {
            echo 'Building initially..'
        }
    
        stage('Test') {
            echo 'Testing phase..'
            try {
                sh 'python3 hello-world.py'
            }
            catch (exc) {
                println 'Failed to run the python script using bash'
            }            
        }
    
        stage('Deploy') {
            echo 'Deploying phase....'
        }
}
