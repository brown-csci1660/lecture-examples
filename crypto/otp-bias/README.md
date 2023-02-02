## Key reuse demo

## Prerequisites

The program uses Python 3 and relies on the `numpy`, and `cv2` Python
packages. If you have the `pip` installer for Python, you can install
these as follows. 

```
pip install opencv-python
pip install numpy
```

Depending on your system, you may need to
install these using the `--user` argument to install the packages for
your local user, or set up a python virtual environment.  

## Overview


In the "Key Reuse" demo, we focused on one way that information can be leaked via incorrect usage of one-time-pads; in particular, key reuse. In this demo, we'll focus on something a little different, but still related to the idea that, even though we have this cryptographic primitive that will provably give us "perfect secrecy", subtle things that we do in setting up this primitive can cause us to still inadvertently leak information.

The particular thing that we'll demonstrate here is the pitfalls of using imperfect, or _biased_ random number generators for creating one time pads. The demonstration program was [stream.py]({{ 'files/demos/one-time-pad/stream.py' | relative_url }}).

The program encrypts an image by generating a stream of pseudorandom pixels, and adding it to the image to obtain a ciphertext. You can set the bias of the pseudorandom number generator (PRNG) used to produce this stream using the slider bar. Moving the slider to the left will increase the probabilty that a given bit is 0 while moving the slider to the right will increase the probability that a given bit is 1.

You can invoke the script like this:

```
./stream.py <img file>
```

This program uses openCV to parse images so it will work with any image format supported by the library (`.jpg`, `.jpeg`, `.png`, `.bmp`, ...).

In order to make the UI more responsive, the program computes all key-cipher pairs and caches the results before launching the UI. The encryption is relatively fast, but smaller images will be faster if you are in a hurry.

As demonstrated by the demo program, just getting a little bit of bias in our random generator allows us to recognize even just local patterns within the image. For images, where there are many visual patterns everywhere, these patterns can easily reveal certain information about our image to the human eye. For text, it's a little more difficult, but it's possible to do things like the cryptanalysis described when we discussed the Caesar cipher that reveal some information within the plaintext, since human languages are not completely random strings of characters.

