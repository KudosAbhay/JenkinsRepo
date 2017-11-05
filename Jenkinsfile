node {
    
        stage('Build') {
            println 'Building initially..'
        }
    
        stage('Test') {
            println 'Testing phase..'
            try {
                sh 'python3 hello-world.py'
            }
            catch (exc) {
                println 'Failed to run the python script using sh command'
            }            
        }
    
        stage('Deploy') {
            println 'Deploying phase....'
        }
}
