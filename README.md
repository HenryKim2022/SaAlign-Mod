# SaAlign

## Software/Tools that Need to be Installed

1. [Oracle Virtual Machine Lastest ver(for Windows)](https://download.virtualbox.org/virtualbox/7.0.10/VirtualBox-7.0.10-158379-Win.exe)
2. [Linux OS lastest ver(im using Kali Linux)](https://mirror.primelink.net.id/kali-images/kali-2023.3/kali-linux-2023.3-installer-amd64.iso)
3. VSCode for Linux lastest ver

   ### download & install VSCode(CLI):

   ```
   wget -O vscode.deb https://code.visualstudio.com/sha/download\?build\=stable\&os\=linux-deb-x64
   sudo dpkg -i vscode.deb
   sudo apt install -f
   ```

   ### run VSCode:

   `code`

   ### manual update VSCode:

   ```
   sudo apt update
   sudo apt upgrade code
   ```

4. Python Extension (for Linux VSCode)
   ```
   Do it manually in VSCode Extension Tab, search for 'Python' (it's the most top in list), then click install.
   ```
5. Python v3.11 for Linux lastest ver

   ### install py depedency

   ```
   sudo apt update
   sudo apt install -y build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
   libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
   ```

   ### install the PY IDE(advanced method)

   ```
   wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
   tar -xf Python-3.11.0.tgz
   cd Python-3.11.0 6. Pyspark lastest ver libraries for Python
   ```

6. Java JDK for Linux

   ### Check Java Ver

   ```
   java -version
   ```

   If the linux not have Java Installed do install it using CLI below.

   ### install java JDK

   ```
   sudo apt update
   sudo apt install default-jdk
   ```

   ### set JAVA_HOME

   ```
   export JAVA_HOME=/usr/lib/jvm/default-java # Adjust the path if needed
   export PATH=$PATH:$JAVA_HOME/bin
   ```

   ### restart terminal

   ```
   source ~/.bashrc # or source ~/.zshrc for Zsh

   ```

7. Pyspark Libraries for VSCode lastest ver
   In Linux VSCode, open terminal then type:

   ```
   pip install pyspark
   ```

   Then, in the Linux Terminal:

   ```
   wget https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
   tar -zxvf spark-3.1.2-bin-hadoop3.2.tgz
   sudo mv spark-3.1.2-bin-hadoop3.2 /opt/spark
   export SPARK_HOME=/opt/spark
   export PATH=$PATH:$SPARK_HOME/bin
   source ~/.bashrc  # or source ~/.zshrc for Zsh
   cd /opt/spark/conf
   cp spark-env.sh.template spark-env.sh
   cp spark-defaults.conf.template spark-defaults.conf
   spark-shell

   ```

   ### Note: This Libraries is a must to be Pre Installed

   [pyspark](https://spark.apache.org/docs/latest/api/python/) ---must be compatible with the corresponding Python version to run

   PySpark is an interface for Apache Spark in Python. It not only allows you to write Spark applications using Python APIs, but also provides the PySpark shell for interactively analyzing your data in a distributed environment. PySpark supports most of Spark’s features such as Spark SQL, DataFrame, Streaming, MLlib (Machine Learning) and Spark Core.

## Instruction

1. Download **SaAlign mod** from website： https://github.com/HenryKim2022/SaAlign-Mod.
2. Make sure all software/tools listed above done well.
3. When writing Python scripts,Using Python statements: `from SaAlign import sa_align`, Using sa\_ align for MSA operation.

## Parameter details for RUN.py:

### Local Node Examples

```py
sa_align(memory,application_name,filename,basepath,partition = 1,url = "local[*]")
```

### Spark Cluster Example

```py
sa_align(memory,application_name,filename,basepath,partition = 1,url = "url of your spark cluster")
```

## Parameter description

### memory

The memory allocated by each executor. The allocation of this parameter will affect the running success or not.
eg."2g","512m"

### application_name

The name of the starting task.
eg."SaAlign_MultipleDNAorRNA"

### filename

Name of fasta file for MSA operation
eg."covid_10.fasta"

### basepath

After extracting **_the downloaded SaAlign_Mod_** ,the path of **_SaAlign.py_**

### partition

The number of all partitions specified when running the program,which can be specified by yourself
default = 1

### url

When running the program, the URL address of the spark cluster (eg."spark://192.132.232.1:7077"). The default address is localhost,that is, `local [*]` using all CPU cores for calculation.

## Output

- Sequence file after completing MSA (Multiple Sequence Analysis)
- Plus, you can use the output file of SaAlign to construct the Polyogenetic Tree with any tool you want like (Raxml, IQTree and etc.)

## Known issues and planned updates

1. Known issues

- There must be a line gap between each sequence in the fasta files.

- The accuracy is good especially for the sequences which are quite different with each other but in this consequence the speed is relatively slow.

1. TODO list

- Offer more options to select the algorithm

## Contact

For bug reports or suggestions, please the original owner at princeyuansql AT gmail DOT com

```

```
