#!/usr/bin/python2.7
from snakebite.client import Client

def createdir(directory_list):
    # Initialize Snakebite client
    client = Client("localhost", 9000)

    try:
        for x in client.mkdir(directory_list):
            print(x)
    except Exception as e:
        print("Error: {}".format(e))

# if __name__ == '__main__':
#     directory_list = ["/Betty", "/Betty/Holberton"]
#     createdir(directory_list)
