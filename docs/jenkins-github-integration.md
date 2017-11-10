***Jenkins - Github - Integration***

This file is referenced from [here](https://wilsonmar.github.io/jenkins-setup/)


<b>To Create a GitHub Token</b>

1.  Login to the GitHub account (which is to be referenced from within Jenkins).
2.  Select Settings.
3.  Select Developer Settings
4.  Click “Personal access tokens”.
5.  Click “Generate new token”.
6.  For Token Description, enter “jenkins”.
7.  Check “repo” and “adminrepo_hook” and all under them.
8.  Click “Generate token”.
9.  Copy the token content to your clipboard.

<b>To Connect this GitHub Account with Jenkins</b>
1.  Go to Jenkins server, Manage Jenkins, Global Toll Configuration.
2.  In Git, add Name “Git”, Path: “git” (doesn’t matter). Click Save.
3.  Go to Jenkins server -> Manage Jenkins -> Configure System.
4.  In GitHub section, API URL leave “https://api.github.com”. Click Add,
5.  Select “Secret Text”.
6.  Paste the token obtained from Github
7.  Click “Test Connection”
8.  Save it.
