<h1><u>Implementing DeepLabV3+ using Keras to remove video background without the green screen</u></h1>

<br>

<strong>When to use this project?</strong>
1. If you are going to use Google Colab or any other online service to process your recorded video file then use <code>recorded.py</code>.
2. If you want to process live video streaming from your webcam then use <code>live.py</code>.

<br>

<strong>Why this project blur recoded file?</strong><br>
When you have low end device and you want to use Google Colab to process your file (or you have recorded video in any other device), to avoid unexpected bugs out there you have to use <code>recorded.py</code>

<br>

<strong>What about video sound?</strong><br>
You won't get your audio in the processed file.

<br>

<strong>Then how to merge the audio with the processed file?</strong><br>
You can use any video processing software to grab audio from your original file and paste it over the paste it over processed file and render it.

<br>

<strong>Will I get audio in live video?</strong><br>
No, this project uses computer vision to process video not audio so you have to merge audio file.

<h2>Features</h2>

1. Highly user friendly.

2. Recording live video (without audio).

3. Process your recorded video.

4. Maintainable code.

5. DeepLabV3+ updated for TensorFlow 2.x (fixed error AttributeError: 'int' object has no attribute 'value').<br>
