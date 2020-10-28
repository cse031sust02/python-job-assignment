## Task 1:
To achieve the requirement, what is your step? As a lead what is your plan? Please describe your architecture, database and technical specification and why?

> Please find my notes in [task1](/task1) folder

## Task 2:


#### 1) Write a Django app with celery that will run two iterative tasks task_1(), task_2() and they will sleep for 2 and 3 seconds respectively. These tasks will run in every second.
- Hints: Use celery and Rabbitmq to run the tasks.

> The source code is avialable in [task2](/task2) folder. Main work for this assignment is in this [file](task2/idare/settings.py)

#### 2) Use docker to run the above application.

> Please follow to How to Run instructions to run using docker

#### 3. Write a Django application that will send data to the front-end after every 5 seconds and show the status using bootstrap Progress bar.
- Hints: you can use jquery to load the status from the frontend and show the result
on the front-end.

> I could not complete it fully. First I did not get the idea clearly. Then I tried to complete it with a [Third Party Library](https://github.com/czue/celery-progress). Source code for this part is also in the same repo. I added a [django app](task2/progress_demo) for this assignment. So after you run app using docker, You can see the output for this assignment by going to this url `http://127.0.0.1:8000/progress_demo/` in your browser.
