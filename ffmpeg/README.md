# 🎬 FFmpeg + Python in Google Colab

[![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/your-repo/blob/main/FFmpeg_Colab_Tutorial_v5.ipynb)

This repository contains a **hands-on Google Colab notebook**
(`FFmpeg_Colab_Tutorial_v5.ipynb`) that teaches you how to use
**FFmpeg** (the swiss-army knife of video/audio processing) together
with Python.

If you're new to Python, don't worry! The notebook is built
**step-by-step** with plenty of examples, so you can run the cells,
experiment with parameters, and immediately see the results.

------------------------------------------------------------------------

## 🚀 What is FFmpeg?

[FFmpeg](https://ffmpeg.org/) is an **open-source command-line tool**
used everywhere in media processing. Think of it as the "engine" that
powers video editing, conversion, and streaming behind the scenes.

With FFmpeg, you can:

-   Convert between video/audio formats (e.g. MP4 → GIF, MP4 → MP3)
-   Trim, crop, or resize videos without re-encoding
-   Control compression (quality vs file size)
-   Overlay videos, subtitles, or watermarks
-   Normalize and filter audio
-   Concatenate clips together
-   Generate GIFs or preview thumbnails
-   Work with modern codecs like **H.264, H.265, VP9, AV1, Opus**

------------------------------------------------------------------------

## 📓 What's inside the Colab notebook?

The tutorial notebook (`FFmpeg_Colab_Tutorial_v5.ipynb`) is divided into
sections you can run interactively in Colab:

1.  **Setup**\
    Install FFmpeg and Python helper libraries inside Colab.

2.  **Environment Check**\
    Detect if you're on CPU, GPU, or TPU. (Colab usually gives CPU only
    for FFmpeg encoding.)

3.  **Sample Media**\
    Generate a short synthetic video + audio to practice with.

4.  **Media Inspection** (`ffprobe`)\
    Learn how to inspect codecs, bitrates, duration, and stream info.

5.  **Common Tasks**

    -   Trim videos (fast vs precise cuts)\
    -   Resize, change frame rate\
    -   Concatenate clips\
    -   Burn in subtitles\
    -   Side-by-side or picture-in-picture\
    -   Make animated GIFs

6.  **Compression & Quality**

    -   CRF (quality scale for H.264/H.265)\
    -   Presets (speed vs efficiency)\
    -   Two-pass encoding for exact bitrates

7.  **Filters**\
    Apply scale, crop, pad, brightness/contrast, overlays, and EQ.

8.  **Audio Tools**

    -   Extract or replace audio\
    -   Loudness normalization\
    -   Sidechain compression (ducking music under narration)

9.  **Python Bridges**

    -   Use
        [`ffmpeg-python`](https://github.com/kkroening/ffmpeg-python) to
        build pipelines in Python\
    -   Use OpenCV to read/write frames with Python

10. **Cheat Sheet**\
    Quick reference for useful codecs, flags, and filters.

------------------------------------------------------------------------

## 🧑‍💻 Why run this in Google Colab?

-   **No setup needed**: Just open the notebook in Colab and press ▶️
    Run.\
-   **Free compute**: Use Google's CPU/GPU (though GPU encoding is
    usually disabled for FFmpeg).\
-   **Python + FFmpeg together**: See how shell commands and Python code
    can mix.\
-   **Safe sandbox**: Try risky commands without affecting your
    computer.

------------------------------------------------------------------------

## 🎯 Who is this for?

-   Beginners curious about **video/audio processing**
-   Python learners who want to combine scripting with media tools
-   Content creators who need **batch video editing** or quick format
    conversions
-   Developers who want to automate media pipelines

------------------------------------------------------------------------

## 📂 How to use

1.  Open the notebook in Google Colab:

        FFmpeg_Colab_Tutorial_v5.ipynb

    (Click the Colab badge above to launch it directly from GitHub!)

2.  Run the setup cell to install FFmpeg.

3.  Go through the sections in order. Each code cell is **independent**,
    so you can tweak and rerun to learn.

------------------------------------------------------------------------

## 🌟 Benefits of FFmpeg

-   **Ubiquitous**: Used by YouTube, VLC, OBS, and countless apps.\
-   **Powerful**: Almost anything you can imagine with audio/video is
    possible.\
-   **Cross-platform**: Works on Linux, macOS, Windows, Colab.\
-   **Scriptable**: Perfect for automation with Python.\
-   **Free & Open Source**: Battle-tested and community-driven.

------------------------------------------------------------------------

## 🔑 Key takeaways

-   FFmpeg is your *media Swiss-army knife*.\
-   CRF + presets let you balance quality and file size.\
-   Filters unlock creative and technical transformations.\
-   Python + FFmpeg = automation superpowers.\
-   Colab is a great place to **experiment safely**.

------------------------------------------------------------------------

💡 **Tip:** Once you're comfortable, start replacing the sample video
with your own files and try chaining filters together to see what
happens!
