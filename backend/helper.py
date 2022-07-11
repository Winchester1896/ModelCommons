import docker
import subprocess
import os
import pandas as pd
import ruamel.yaml as yaml

def run_docker_image():
    print('running docker')
    client = docker.from_env()
    client.containers.run("zichenzhang/defonet-train:2.1", 
                        device_requests=[docker.types.DeviceRequest(count=-1, capabilities=[['gpu']])],
                        detach=False,
                        stdout=True
                        )
   

def call_docker_image():
    cmd = 'docker run --privileged --rm --gpus all -v $PWD/../docker-testbench:/tmp/data -e t0=200 zichenzhang/defonet-train:2.2'

    returned_value = subprocess.call(cmd, shell=True)

    print(returned_value)


def readCSV(filename):
    data= pd.read_csv(filename)
    return data

def appendToDF(df1, df2):
    df = df1.append(df2, ignore_index=True)
    return df

def saveDfToFile(df, filename):
    df.to_csv(filename, index=False)

def readYAML(filename):
    with open(filename, 'w') as f:
        yf = yaml.safe_load(f) # dict
    f.close()
    return yf


def getFileType():
    split_tup = os.path.splitext('my_file.tar.gz')
    print(split_tup)
    
    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    
    print("File Name: ", file_name)
    print("File Extension: ", file_extension)

