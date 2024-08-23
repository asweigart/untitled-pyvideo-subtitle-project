# untitled-pyvideo-subtitle-project
Creating better transcripts/subtitles for PyCon videos on YouTube.

This repo collects the work for using Whisper and human-review to create better transcripts for PyCon talks. [PyVideo.org](https://pyvideo.org) has collected uploaded PyCon talks (mostly hosted on YouTube) and organized their metadata [in their "data" repo.](https://github.com/pyvideo/data)

This project builds on these efforts to make accessible, searchable text of these talks available.

We use yt-dlp to download the talk's video, extract the audio, have Whisper produce the initial transcription, use ChatGPT to identify likely problem spots, have a human review the transcription, then hand it to channel owners to include on their videos and to PyVideo.org to make the talks searchable.


Contribute
==========

You can get involved! This project needs people who can:

- Leave Whisper running on their computers to transcribe talks.
- Provide human-review of the automated transcriptions.
- Reach out to conference organizers and YouTube channel owners who will add the subtitles to their videos.

Please reach out to the maintainers before starting so that we don't duplicate efforts:

Al Sweigart [al@inventwithpython.com](mailto:al@inventwithpython.com) [https://mastodon.social/@AlSweigart](https://mastodon.social/@AlSweigart)

Process
========

Before you begin:

- It's a good idea to read [this guide on creating subtitles for videos.](https://uxdesign.cc/a-guide-to-the-visual-language-of-closed-captions-and-subtitles-2fda5fa2a325)
- Make sure you are in contact with the YouTube channel owner *before* starting to transcribe videos.
- Download the zip of PyVideo's ["data" repo](https://github.com/pyvideo/data/archive/refs/heads/main.zip) and put the data/ folder in the root of this project's repo. (This step only needs to be done once. Do not commit these files to the repo. They're used by the Python scripts.)
- You'll need to understand how to use the command-line terminal and activate Python virtual environments. (If you don't know how to do this, you can still do the more important work of human-reviewing the transcripts.)

The process of creating subtitles for this project:

- Open a terminal window and activate the virtual environment for this project. (The Python scripts need the latest `yt-dlp` and `openai-whisper` packages.)
- Run the `download_pycon_talks.py` script with a command line argument of the events whose talks you want to download. These names are in the data/ folder and are like "pycon-us-2019" or "pytexas-2024". (There are over 400 events, each with dozens of talks.) Do not add the .m4a audio files to the git repo.
- Run the `whisper_pycon_talks.py` script with a command line argument of an event. This will run Whisper with the "medium" model to produce an .srt subtitle file for each of the event's talks. Two copies of the transcripts are made with names like `pytexas-2024/talk-name.srt` and `pytexas-2024/originals/talk-name.srt` so that the original Whisper transcription is always available.
- Delete the .m4a audio files of the talks; they are no longer needed.
- Get a list of potential transcription errors that the human reviewer should check for. Copy and paste the Whisper transcript into ChatGPT with the following prompt: *The following is the machine-produced .srt transcrption of a PyCon conference talk. Identify any terms that could have likely been incorrectly transcribed, especially proper names, acronyms, or technical jargon:*
- Put this output into a file with a name like `pytexas-2024/human-reviewer-notes/talk-name.srt`.
- Using these notes, read through the transcription and make needed corrections. If there are many errors, you may need to play the original talk video (on 2x speed) while reading along to get context, or look up talk info to get things like the correct spelling of the speaker's name.
- Commit the corrected .srt transcript. (We'll use the existence of this file in the repo as a sign that it is finished. Please don't commit half-finished .srt files.)
- Send the videos to the YouTube channel owner so they can add them to the video.

In the future, we'll be adding these transcripts to the PyVideo repo so that they can be searchable on that site. We'll also create translations of these subtitles to non-English languages.
