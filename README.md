## Video Steg

This is a simple tool used for sending data through Video Files. 

### Installation
It needs [OpenCv2](https://pypi.org/project/opencv-python/) which is used for getting the frames of the video file. 

You can use this

```
$ pip install -r requirements.txt
```
or manually install it.

### How to use

[![asciicast](https://asciinema.org/a/KE2Ix2pUzej8iBEqceDPSEUBb.png)](https://asciinema.org/a/KE2Ix2pUzej8iBEqceDPSEUBb)

### Theory

Every Video is nothing but a collection of frames(or just images). We can use various techniques of Image Steg on each of this frame. This tool just uses that concept and creates a very simple way of hiding information in each frames. 

Every frame(or image) is just a grid of RGB values (also RGBA depending on the type of image). Each of the R, G, B channel has values ranging from 0-255. Clearly we can represent ASCII chars for each of these values. 

![RGB pixel](https://media.geeksforgeeks.org/wp-content/uploads/Pixel.jpg)

But data can be anything not just ASCII chars, so we need to find a way of encoding that data, in this case I have used [Base32](https://en.wikipedia.org/wiki/Base32) encoding for that. 

### Encryption Process

1. Convert the secret data to base32
2. Go through every pixel in a frame and look for a particular char value in a particular channel. 
3. Note down the pixel postion. 

After the encryption we will have a CSV file which will have all the positions of the pixels which represent the encoded secret message. We can simply reverse the process to get back the data. 


### Pros:
1. Large Amount of Information can be stored and shared because Video's have large number of frames. To give an idea, a 5min video has 300 seconds. And if the video resolution is 480p (854x480) and is running on 30fps then it has 3689280000 pixels. If you use all the 3 channels you have 11067840000 bytes(11.06784 Gb ) of information. 
2. All you need to transfer is the index values and you can choose any video online. 
3. To decode the secret one needs to have both the video as well as the dictionary file. 

### Cons:
1. The size of the dictionary.csv is proportional to the length of the encoded has of the secret data. 
2. In any normal video there is usually not much distinction between different frames. The pixel data remains the same almost. As the result there is not much entropy or randomness. 


This is just a concept, not at all a practically useful too. Please feel free to contribute. 
