#!/bin/bash
####################################
#
# Error Informing Script for JenkinsRepo.
# Let's post the Error as a Slack Message
#
####################################
CURL='/usr/bin/curl'

curl -X POST \
  https://slack.com/api/chat.postMessage \
  -H 'authorization: Bearer abc' \
  -H 'content-type: application/json; charset=utf-8' \
  -d '{
  "channel":"#pipelineerror",
  "text":"Testing phase Error in JenkinsPipeline",
  "as_user":"abhay"
}'
