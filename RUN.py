from SaAlign import sa_align
import os

current_script_directory = os.path.dirname(os.path.abspath(__file__))

memory = "1g"  # 1g or 512m
application_name = "SaAlign_MultipleDNAorRNA"  # App Name
filename = "./dataset/covid_10.fasta/"  # Data Set
basepath = current_script_directory     # Current Directory

sa_align(memory, application_name, filename,
         basepath, partition=2, url="local[*]")
