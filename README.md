<h1><u>Implementing DeepLabV3+ using Keras to remove video background without green screen</u></h1>

<strong>When to use this proect?</strong><br>
1. If you are going to use Google Colab or any other online service to process your reocrded video file then use <code>recorded.py</code>. <br>
1. If you want to process live video streaming from your webcam then use <code>live.py<code>. <br>

<strong>Why this project blur recoded file?</strong><br>
When you have low end device and you want to use Google Colab to process your file (or you have recorded video in any other device), to avoid unexpected bugs out there you have to use <code>recorded.py</code><br>

<strong>What about video sound?</strong><br>
You won't get your audio in the processed file.<br>

<strong>Then how to merge the audio with the processed file?</strong><br>
You can use any video processing software to grab audio from your original file and paste it over the paste it over processed file and render it.<br>

<strong>Will I get audio in live video?</strong><br>
No, This project uses computer vision to process video not audio so you have to merge audio file.<br>

<h2>Features</h2><br>
1. Highly user friendly.<br>

2. Recording live video (without audio).<br>

3. Feature to use project for recorded file.<br>

4. Maintainable code.<br>

5. DeepLabV3+ for for tensorflow 2.x (fixed error AttributeError: 'int' object has no attribute 'value').<br>
