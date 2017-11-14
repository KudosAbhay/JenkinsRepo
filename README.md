# JenkinsRepo
First trial for Jenkins

Workflow:

1.  Checks if User is on Linux or Windows
2.  Depending on the OS, executes the following flow
3.  Alerts via Slack in particular stages if errors persist

<br>

1.  Enters Stage 'Build': <br>
    <i>Catches any errors if present - messages on Slack accordingly</i>
2.  Enters Stage 'Test': <br>
    <i>Catches any errors if present - messages on Slack accordingly</i>
    <i>Mentiones phase completion for next stage if 'Test' is successful
3.  Enters Stage 'Deploy from OS':<br>
    <i>Copies the current build to prod folder</i>
