
# Server Usage

This document explains how to run scripts on our deep learning servers. This assumes you are already logged in via `ssh`.

## Datasets

Please do not upload datasets to the server. All required datasets are available inside the `datasets/` folder in your home directory. If you need another dataset for some reason, please ask us first.

## Task Scheduling

While our servers are powerful, task scheduling is required because training a CNN typically results in full utilization of a single GPU. Each server has four GPUs so at most four processes that require GPU resources should run in parallel and on different GPUs. The task scheduler ensures this.

### Submitting Jobs

To schedule a job that requires access to the GPU, create a bash script that includes the corresponding commands. The first lines must always be as follows:

```bash
#!/bin/bash
#PBS -S /bin/bash  
#PBS -m bea
#PBS -M <your_email>

# Request free GPU
export CUDA_VISIBLE_DEVICES=$(getFreeGPU)
```

**Computationally expensive (training) scripts must use CUDA, make sure you enable this via e.g. `net.cuda()`.**

Change `<your_email>` to an email address to which notifications should be sent. The scheduler will notify you if your script starts and when it has finished. The `export` line is always required in this exact form. It ensures that your scripts will run on the GPU that is currently utilized the least.

Afterwards, simply add the command(s) to execute, one per line, e.g.:

    python3 my_python_script_that_requires_gpu.py

Once the script is ready, submit it to the scheduler like so:

    qsub my_script.sh

### Job Administration

Use `qstat` to view your job queue. It will return something like this:

    Job id                    Name             User            Time Use S Queue
    ------------------------- ---------------- --------------- -------- - -----
    69.localhost              test.sh          stefan          00:00:00 C batch
    70.localhost              test.sh          stefan                 0 R batch
    71.localhost              test.sh          stefan                 0 Q batch
    72.localhost              test.sh          stefan                 0 Q batch

The `S` column shows the job status:

    C     job is completed
    R     job is running
    Q     job is waiting the queue

If you want to cancel a job, use `qdel JOB`, with `JOB` being the Job ID shown in `qstat`.

### Accessing Job Output

If your scripts log to the console (usually), you might want to retrieve this output once the job has finished. The scheduler writes all such output to a file called `JOBNAME.oJOBID` in the working directory once the job starts to run.

### Don't Cheat

Do not attempt to bypass the scheduler by executing your scripts directly. The server will detect this and kill the corresponding process. Also don't chain several long-running commands inside a single job script. There is a time limit after which every job will be killed (1 hour). Basically, be fair and share the limited resources we have with your colleagues.

### Limited Resources and Queues

We expect queues will fill up close to assignment deadlines. In this case, you might have to wait a long time before your script even starts. In order to minimize wait times, please do the following:

* Write and test your code locally on your system. If you have a decent Nvidia GPU, please train locally and don't use the servers. If you don't have such a GPU, perform training for a few epochs on the CPU to ensure that your code works. If this is the case, upload your code to our server and do a full training run there. To facilitate this process, have a variable or a runtime argument in your script that controls whether CUDA should be used. Disable this locally and enable it on the server.
* Don't schedule multiple training runs in a single job, and don't submit multiple long jobs. Be fair.
* If you want to train on the server, do so as early as possible. If everyone starts two days before the deadline, there will be long queues and your job might not finish soon enough.
