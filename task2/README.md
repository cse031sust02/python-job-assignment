- clone the repository
```bash
pc:~$ git clone https://github.com/cse031sust02/idare-task.git
```

- enter directory named task2
```bash
pc:~$ cd task2
```

- run docker compose
```bash
pc:~/task2$ docker-compose up
```

- view the output on the console
```bash
.........
...........
worker_1  | [2020-10-28 01:13:20,584: WARNING/ForkPoolWorker-3] Task 2 is sleeping for three seconds
worker_1  | [2020-10-28 01:13:20,586: INFO/MainProcess] Received task: idare.celery.task_2[bc213e8d-e0d9-42a1-9861-04530b1c3008]  
worker_1  | [2020-10-28 01:13:21,552: INFO/Beat] Scheduler: Sending due task task 2 (idare.celery.task_2)
worker_1  | [2020-10-28 01:13:21,568: INFO/Beat] Scheduler: Sending due task task 1 (idare.celery.task_1)
worker_1  | [2020-10-28 01:13:22,552: INFO/Beat] Scheduler: Sending due task task 2 (idare.celery.task_2)
worker_1  | [2020-10-28 01:13:22,568: INFO/Beat] Scheduler: Sending due task task 1 (idare.celery.task_1)
worker_1  | [2020-10-28 01:13:23,552: INFO/Beat] Scheduler: Sending due task task 2 (idare.celery.task_2)
worker_1  | [2020-10-28 01:13:23,568: INFO/Beat] Scheduler: Sending due task task 1 (idare.celery.task_1)
worker_1  | [2020-10-28 01:13:23,587: INFO/ForkPoolWorker-3] Task idare.celery.task_2[d8103de5-1002-4d63-a854-b32a836200ed] succeeded in 3.0035599029997684s: None
worker_1  | [2020-10-28 01:13:23,593: WARNING/ForkPoolWorker-3] Task 1 is sleeping for two seconds
worker_1  | [2020-10-28 01:13:23,598: INFO/MainProcess] Received task: idare.celery.task_1[6ea7175b-91df-4c72-a57b-b1a3bc0c484c]  
worker_1  | [2020-10-28 01:13:24,553: INFO/Beat] Scheduler: Sending due task task 2 (idare.celery.task_2)
worker_1  | [2020-10-28 01:13:24,569: INFO/Beat] Scheduler: Sending due task task 1 (idare.celery.task_1)

```