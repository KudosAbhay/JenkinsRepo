node {
    
        stage('Build') {
            echo 'Building initially..'
            System.properties['os.name']
            if (System.properties['os.name'].toLowerCase().contains('windows')) {
                println "it's Windows"
            } else {
                println "it's not Windows"
            }
        }
    
        stage('Test') {
            echo 'Testing phase..'
            try {
                sh 'python3 hello-world.py'
            }
            catch (exc) {
                echo 'Failed to run the python script using bash'
            }            
        }
    
        stage('Deploy') {
            echo 'Deploying phase....'
        }
}
