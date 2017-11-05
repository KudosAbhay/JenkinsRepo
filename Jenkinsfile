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
                sh 'C:\Users\abhay\AppData\Local\Programs\Python\Python35-32\python.exe sendErrorMessage.py'
            }            
        }
    
        stage('Deploy') {
            println 'Deploying phase....'
        }
}
