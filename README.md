<h1><u>Implementing DeepLabV3+ using Keras to remove video background without green screen</u></h1>

If you are going to use Google Colab or any other online service to process your reocrded video file then use <code>recorded.py</code>.\n
If you want to process live video streaming from your webcam then use <code>live.py<code>.\n\n

<strong>Why this project blur recoded file?</strong>\n
When you have low end device and you want to use Google Colab to process your file (or you have recorded video in any other device), to avoid unexpected bugs out there you have to use <code>recorded.py</code>\n

<strong>What about video sound?</strong>\n
You won't get your audio in the processed file.\n

<strong>Then how to merge the audio with the processed file?</strong>\n
You can use any video processing software to grab audio from your original file and paste it over the paste it over processed file and render it.\n

<strong>Will I get audio in live video?</strong>\n
No, This project uses computer vision to process video not audio so you have to merge audio file.\n

<h2>Features</h2>\n
1. Highly user friendly.\n
2. Recording live video (without audio).\n
3. Feature to use project for recorded file.\n
4. Maintainable code.\n
5. DeepLabV3+ for for tensorflow 2.x (fixed error AttributeError: 'int' object has no attribute 'value').\n
