<h1><u>Implementing DeepLabV3+ using Keras to remove video background without green screen</u></h1>

This project can blur only recorded file but if you want to blur background live then just replace the code of <code>main.py</code> by the code given at this <a href='https://github.com/zubairahmed-ai/Live-Background-Blur/blob/master/LiveBackgroundBlur.py'>link</a>

<strong>Why this project can only blur recoded file?</strong>
When you have low end device and you want to use Google Colab to process your file. So to avoid unexpected bugs out there I have modified the code.

<strong>What about video sound?</strong>
You won't get your audio in the processed file.

<strong>Then how to merge the audio with the processed file?</strong>
You can use any video processing software to grab audio from your original file and paste it over the paste it over processed file and render it.

<h2>Features</h2>
1. Highly user friendly.
2. DeepLabV3+ for for tensorflow 2.x (fixed error AttributeError: 'int' object has no attribute 'value').
