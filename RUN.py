from SaAlign import sa_align
import os

current_script_directory = os.path.dirname(os.path.abspath(__file__))

# memory = "512m"   #512MB RAM
memory = "1g"  # 1GB RAM
application_name = "SaAlign_MultipleDNAorRNA"  #
filename = "./dataset/covid_10.fasta/"
basepath = current_script_directory

sa_align(memory, application_name, filename,
         basepath, partition=2, url="local[*]")
