***To Create a New Pipeline:***

1.  In General Tab, Checked Github Project, provided project url
2.  In Build Triggers, Checked Github Pull Requests: Trigger Mode: Cron Persisted data
3.  Also checked Github hook trigger for SCM Polling
4.  In Pipeline Tab, Selected Pipeline Script from SCM (which will check for Jenkinsfile in git repo)
5.  In SCM, Select Git, Enter Repo url and git credentials, Branch to build: */master
6.  In Script path, use 'Jenkinsfile'


<br>
Observations:
<br>
Errors pertaining:
1.  The webhook for repo KudosAbhay/JenkinsRepo.git on github.com failed to be registered or was removed. 
    More info can be found on the global configuration page. 
    This message will be dismissed if Jenkins receives a PING event from repo webhook or if you add the repo to the ignore list in the global configuration.
 
2.  GitHub Pull Requests Trigger Errors: GitHub Repo Provider Error. Can't find repo provider for ExperimentingPipeline.
    All providers failed: [org.jenkinsci.plugins.github.internal.GHPluginConfigException: GitHubPluginRepoProvider can't find appropriate client for github repo . Probably you didn't configure 'GitHub Plugin' global 'GitHub Server Settings' or there is no tokenswith ADMIN access to this repository.]
         
