#How to run Automation Script :
Please find automation script in below path: https://github.com/dsekar12/gl_assignment/tree/master/src/test/suite/Automation
Steps to run the script:
Copy the Automation Folder to your local where docker is available and user needs permission to execute the docker.
Run following commands:
  cd Automation
  docker build -t selenium
  
Once docker is built, please see docker images is available by running "docker images" command.
Please run using "docker run -it selenium "

Test Result(Screenshots for Failure and Test Result Logs ) are placed in /usr/src/app/Test_Result/ Folder insde the container.
To make the test result persistent, either we can push to AWS S3 by enable CMD sh aws_s3_push.sh script in Dockerfile or run a docker cp container_id:/usr/src/app/Test_Result/ <localhost_path>


#Please find user story in https://github.com/dsekar12/gl_assignment/blob/master/src/test/resources/requirements/User%20Story.feature
#Please find test plan and test cases in  https://github.com/dsekar12/gl_assignment/tree/master/src/test/suite

