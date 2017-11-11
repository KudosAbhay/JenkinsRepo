node 
{
    phase_completion = 'false'
    if(isUnix())
    {
        //Linux or Mac OS
        stage('Build') 
        {
            try
            {
                println 'Building initially..'
                currentBuild.result = 'SUCCESS'
            }
            catch (exc) 
            {
                currentBuild.result = 'FAILURE'
            }
        }

        switch(currentBuild.result)
        {
            case 'SUCCESS':
                stage('Test')
                {
                    println 'Build successfully. Testing phase...'
                    try
                    {
                        sh 'sh script.sh'
                        sh 'python3 PythonProject/hello.py'
                        sh 'go run GoProject/hello.go'
                        // sh 'python3 sendSuccessMessage.py'
                        phase_completion = 'true'
                    }
                    catch(exc)
                    {
                        currentBuild.result = 'FAILURE'
                        println 'Failure in Testing phase'
                    }
                }
                break
                
            case 'FAILURE':
                currentBuild.result = 'FAILURE'
                println 'Failure in Building phase'
                // bat 'python sendErrorMessage.py'
                break
        }
    }
    else
    {
        //Windows OS
        stage('Build') 
        {
            try
            {
                println 'Building initially..'
                currentBuild.result = 'SUCCESS'
            }
            catch (exc) 
            {
                currentBuild.result = 'FAILURE'
            }
        }

        switch(currentBuild.result)
        {
            case 'SUCCESS':
                stage('Test')
                {
                    println 'Build successfully. Testing phase...'
                    try
                    {
                        bat 'python PythonProject/hello.py'
                        bat 'go run GoProject/hello.go'
                        // bat 'python sendSuccessMessage.py'
                        phase_completion = 'True'
                    }
                    catch(exc)
                    {
                        currentBuild.result = 'FAILURE'
                        println 'Failure in Testing phase'
                    }
                }
                break
                
            case 'FAILURE':
                currentBuild.result = 'FAILURE'
                println 'Failure in Building phase'
                // bat 'python sendErrorMessage.py'
                break
        }
    }

}


node
{
    if(isUnix() && phase_completion == 'true')
    {
        stage('Deploy from Linux') 
        {
            println 'Final Deployment will be done'
            // sh 'cp -R ../FreeStyle /home/abhay/Documents/prod/'
        }        
    }
    else if((!isUnix()) && phase_completion == 'true')
    {
        stage('Deploy from Windows') 
        {
            println 'Final Deployment will be done'
            // bat 'xcopy  E:\JenkinsRepo D:\prod /h /s /e'
        }        
    }
    else
    {
        println 'Deployment failed due to incomplete phase completions'
    }
}
