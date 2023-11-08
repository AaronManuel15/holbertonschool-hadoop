#!/usr/bin/python2.7
from snakebite.client import Client

def download(file_list):
    # Initialize Snakebite client
    client = Client("localhost", 9000)

    # sort directory list in reverse order
    directory_list.sort(reverse=True)
    try:
        for x in client.copyToLocal(file_list, '/tmp'):
            print(x)
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == '__main__':
    directory_list = ["/holbies/input/lao.txt"]
    download(directory_list)
