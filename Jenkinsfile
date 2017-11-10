node {

        stage('Build') {
            try {
                println 'Building initially..'
                sh 'git init'
                sh 'git remote add origin https://github.com/KudosAbhay/JenkinsRepo.git'
                sh 'git pull origin master'
            }
            catch (exc) {
                sh 'python3 sendErrorMessage.py'
                println 'Initial Build fail'
            }
        }

        stage('Test') {
            println 'Testing phase..'
            try {
                println 'script.sh not running'
                sh 'python3 PythonProject/hello.py'
                sh 'go run GoProject/hello.go'
                sh 'python3 sendSuccessMessage.py'
            }
            catch (exc) {
                sh 'python3 sendErrorMessage.py'
                println 'Failed in Testing phase'
            }
        }

        stage('Deploy') {
            println 'Deploying phase finally...'
        }
}
