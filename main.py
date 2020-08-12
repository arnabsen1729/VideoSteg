#!/bin/python3

import cv2
from base64 import b32encode, b32decode

message="s3cr3t_m3554g3"
msg_len=0
color_channel=0

def findIndex(image, msg_char):
    height, width, channel = image.shape
    global msg_len
    for i in range(height):
        for j in range(width):
            red_val = image[i][j][color_channel]
            if(ord(msg_char)==red_val):
                msg_len+=1
                return (i, j)

def encryptData(path):  
    vidObj = cv2.VideoCapture(path) 
    count = 0
    outputFile = open('dictionary.csv', 'w')

    while msg_len < len(message): 
  
        breakPoint, image = vidObj.read() 
        if not breakPoint:
            break

        index = findIndex(image, message[msg_len])
        if index==None:
            print('There is a problem with this video. Choose another one...')
            exit(0)

        outputFile.write('({x}, {y})\n'.format(x=index[0], y=index[1]))
        count += 1
    print('DONE')

def decryptData(path, file):  
    try:
        vidObj = cv2.VideoCapture(path) 
        count = 0
        outputFile = open(file, 'r')
        data = outputFile.read().split('\n')
        index = []
        for val in data:
            if len(val)==0:
                break
            fval = int(val[1:val.find(',')])
            sval = int(val[val.find(',')+1: -1])
            index.append((fval, sval))
        
        result_msg=''
        for val in index:
            breakPoint, image = vidObj.read() 
            if not breakPoint:
                break
            result_msg += str(chr(image[val[0]][val[1]][color_channel]))

        f = open('result.txt', 'w')
        f.write(b32decode(result_msg.encode()).decode())
        print('DONE')
    except:
        print('Make sure you have entered the correct input...')
        exit(0)


if __name__ == '__main__': 
    
    print('1. Encrypt\n2. Decrypt\n Choice: ')
    try:
        choice = int(input())
    except:
        print('Invalid Input!!')
    
    if choice == 1:
        print('Enter Secret Message: ')
        message = b32encode(input().encode()).decode()
        print('Enter path to Video File')
        filePath = input()
        print('Enter color channel(0-> Red, 1-> Blue, 2->Green)')
        color_channel = int(input())
        encryptData(filePath)
    elif choice == 2:
        print('Enter path to Video File')
        filePath = input()
        print('Enter path to dictionary file')
        dictPath = input()
        print('Enter color channel(0-> Red, 1-> Blue, 2->Green)')
        color_channel = int(input())
        decryptData(filePath, dictPath)
