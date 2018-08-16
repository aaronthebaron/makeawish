# Hold Your Breath, Make A Wish, Count To Three  


## System Description

All items here are inside of a VPC called wonka. I went a little hard on the wonka theme, just couldn't get it out of my head. I decided to run a particular job instead of a generic linux command, but it's essentially the same thing. One could structure the command and arguments in the queue entry in multiple ways.

### User Input

An ASG with 1 member that runs a single webpage in nginx. The page has a button that says, "Hold your breath, make a wish, country three". The button runs the `holdyourbreath.py`.

The webserver can also reach out to an S3 bucket where results are stored and display them.

### Job Queuing

The `holdyourbreath.py` puts a request directly in the SQS queue named `wishes`. Since this is a silly example, the queue message is just some text, would most likely be instructions of some sort in a real case. The queue is a normal queue, but there are some good arguments for the queue being a FIFO queue in the standard case you might use this for.

### Handing Out Homework

The queue item will be tied with a lambda function, so that all entries get sent to it. The lambda function runs `makeawish.py` and gets items from the queue and runs containers using Fargate. I choose this for simplicity, but it could be done a lot of ways. Using some pricing/demand logic to call up spot instances is probably the cheaper way to do it. 

### Work

The `counttothree.py` runs in a container on systems managed by Fargate. There is an ECR task called `counttothree` which is used to create the Fargate worker.


### Scaling

There are a couple of ways to scale out. If we need more counting to happen for each request, we could run more processes per request. If we need to run many different jobs then adding to the queue will just run the Lambda function more times resulting in running more counts. Each of these has a monetary cost of course.


### Questions

#### Downsides

- There may be increased costs with Fargate or other technologies that can get reduced using some other method.   
- This seems to work okay for certain types of jobs but maybe not for more complex items, like jobs tied together.
- Reporting results seems wonky this way. There would need to be a better way to gather and distribute results especially if the task were varied greatly in content and source.

#### Alternatives

Infinite. I can think of a billion ways to do this with various pros and cons, many of them are way out bonkers ideas. A lot of it would be more around balancing costs in AWS than actual ability to scale process.

#### CI/CD

This is a pretty simple setup, so it might be nice to have complete test pipeline. I would test each stage of the pipeline, making sure that each unit was tested, but also a nice regression suite of previous jobs and expected output to test the full pipeline against. Once tests were passed it would be simple to build a container, and update the lambda function with a lambda deployment.

#### Results

It seems like the easiest way to get results back to the original machine might be to write them to S3 and either poll for them from a browser, or otherwise notify of results like through a chatops system, email, etc. It also might be possible to put them in a queue as well and have something notifying for results. 

#### Dependent Results

There are maybe some better ways to do this, but since we're using ECS we can actually track task completion. We might construct another Lambda function that listens for a CloudWatch task complete event and can then check the status, slurp up the records and pass it back into the queue as a new/different job. The details would depend on the jobs we have and the format of the results but they could probably be constructed in a generic way. 


