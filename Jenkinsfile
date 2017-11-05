node {
    
        stage('Build') {
            try {
                echo 'Building initially..'
                sh 'python3 hello-world.py'
            }
            catch (exc){
                echo 'Failed to do so'
            }     
        }
    
        stage('Test') {
                echo 'Testing phase..'
        }
    
        stage('Deploy') {
                echo 'Deploying phase....'
        }
}
