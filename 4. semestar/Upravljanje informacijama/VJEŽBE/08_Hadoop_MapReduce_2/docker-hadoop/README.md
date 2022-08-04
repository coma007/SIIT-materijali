# Hadoop on Docker

>Note
Please pull the latest code by using `git pull` before try to run.

See [Standalone mode](https://github.com/wxw-matt/docker-hadoop/blob/master/hadoop-standalone/README.md)


How to Run Hadoop on macOS (Apple M1 and Intel CPU) by One Command

## Platforms supported
ARM64 (Apple Silicon) and AMD64 (Intel)

## Requirement
Docker Desktop is required (and it is the easiest way to get Docker work on your laptop).
For macOS (Apple M1), [Docker Desktop](https://desktop.docker.com/mac/main/arm64/Docker.dmg)
For macOS (Intel), [Docker Desktop](https://desktop.docker.com/mac/main/amd64/Docker.dmg)

### Docker Test
If Docker Desktop is installed properly, you should be able to run the following command:
```
docker run hello-world
```
And see the output like:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
... ...
```

## Start Hadoop Cluster
Go to terminal and clone the git repo to your computer:

```bash
git clone git@github.com:wxw-matt/docker-hadoop.git ~/docker-hadoop
cd ~/docker-hadoop
docker-compose up -d
```
It takes a few minutes to completely start the whole Hadoop cluster for the first time.

## How to Copy Files from Host Computer to HDSF and HDFS to Local System

For example, if you want to copy a file called `Test.txt` from the host computer to HDFS, the file first should be copied to `./jars/data` and you can use the command: `./hdfs dfs -copyFromLocal -f /app/data/Test.txt /input/` to copy it to `/input` in HDFS.

The directories mappings between your computer and the container are:
```
./jobs/jars => /app/jars
./jobs/data => /app/data
./jobs/res => /app/res
```
That means any files in `./jobs/jars` are accessibile in the container through the path `/app/jars`,
any files in `./jobs/data` are accessibile in the container through the path `/app/data`. 

Example:
```bash
# !! Go to docker-hadoop directory first
# Create a file on the host computer
cat > mytest.txt <<EOF
This is the first line.
This is the second line.
The last line comes here.
EOF

# Copy it to ./jobs/data
cp mytest.txt ./jobs/data
./hdfs dfs -mkdir -p /mytest_input
./hdfs dfs -copyFromLocal -f /app/data/mytest.txt /mytest_input/
./hadoop fs -cat /mytest_input/mytest.txt
# Remove the output directory, otherwise you may get an error "Output directory hdfs://namenode:9000/mytest_output already exists"
./hdfs dfs -rm -r -f /mytest_output
# Run a job
./hadoop jar jars/WordCount.jar WordCount /mytest_input /mytest_output
# Remove local output directory
rm -rf ./jobs/res/mytest_output
# Copy output to your computer
./hdfs dfs -copyToLocal /mytest_output /app/res/
# View output from host computer
cat ./jobs/res/mytest_output/*
```

## Run the Example Map-Reduced Job on the Cluster

Run example wordcount job. 
The `WordCount.jar` is located in `./jobs/jars` directory . 

Typing the command below to commit the job.
```
./hdfs dfs -mkdir -p /input
./hdfs dfs -copyFromLocal -f /app/data/README.txt /input/
./hadoop jar jars/WordCount.jar WordCount /input /output
# View output (double quote is needed for zsh when star/asterisk occurs)
./hadoop fs -cat "/output/*"
```
>Note
You may need to remove `/output` first if it already exists using command `./hadoop fs -rm -r /output`.

## Monitor Hadoop Cluster by WebUI

Namenode:  http://localhost:9870

Datanode:  http://localhost:9864

Resourcemanager:  http://localhost:8088

Nodemanager:  http://localhost:8042

Historyserver:  http://localhost:8188

>Note
If you are redirected to a URL like `http://119e8b128bd5:8042/` or `http://resourcemanager:8088/`, change the host name to localhost (i.e. `http://localhost:8042/`) and it will work.
This is because Docker containers use their own IPs which are mapped to different names.

## Common Hadoop Comamnds
```bash
# Create a directory
./hdfs dfs -mkdir -p directory-name
# Remove a directory and its sub-directories
./hadoop fs -rm -r -f directory-name
# Copy files from jobs/data to HDFS
./hdfs dfs -copyFromLocal -f /app/data/README.txt /input/ 
# View files
./hdfs dfs -ls /input 
```

## How to Run Your Own Jobs 

Using `Eclipse` or other IDEs to generate a `jar` file. Copy it to `./jobs/jars`. For example, if your `jar` file name is `HelloWorld.jar` and it is in the `./jobs/jars`. The following command will submit your job to Hadoop.
```
./hadoop jar jars/HelloWorld.jar HelloWorld /input /output
```

And your data will go to `./jobs/data`, then using `./hdfs dfs -copyFromLocal` to copy it to HDFS.


# Credits
The repo is inspired by [@big-data-europe](https://github.com/big-data-europe/docker-hadoop). Without their work, it may take me days to get this done.


# References:
1. https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html