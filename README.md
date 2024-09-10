# untitled-pyvideo-subtitle-project
Creating better transcripts/subtitles for PyCon videos on YouTube.

This repo collects the work for using Whisper and human-review to create better transcripts for PyCon talks. [PyVideo.org](https://pyvideo.org) has collected uploaded PyCon talks (mostly hosted on YouTube) and organized their metadata [in their "data" repo.](https://github.com/pyvideo/data)

This project builds on these efforts to make accessible, searchable text of these talks available.

We use yt-dlp to download the talk and extract the audio, use Whisper to produce the initial transcription, use ChatGPT to identify likely errors, use human review for the final transcription, then hand it to over channel owners to include on their videos and to PyVideo.org to make the talks searchable.


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
- Have a text file open on your computer to take random notes about your experience with this process, and any comments you can make to help us improve it for other transcribers.

The process of creating subtitles for this project:

- Open a terminal window and activate the virtual environment for this project. (The Python scripts need the latest `yt-dlp` and `openai-whisper` packages.)
- Run the `download_pycon_talks.py` script with a command line argument of the events whose talks you want to download. These names are in the data/ folder and are like "pycon-us-2019" or "pytexas-2024". (There are over 400 events, each with dozens of talks.) Do not add the .mp4 video files to the git repo. You may need several gigabytes free to contain all the video files, depending on the size of the conference.
- Run the `whisper_pycon_talks.py` script with a command line argument of an event. This will run Whisper with the "medium" model to produce an .srt subtitle file for each of the event's talks. Two copies of the transcripts are made with names like `pytexas-2024/talk-name.srt` and `pytexas-2024/originals/talk-name.srt` so that the original Whisper transcription is always available.
- Keep the .mp4 video files of the talks if you are going to review the transcriptions. (There's less lag pausing/unpausing them locally while you fix transcriptions, compared to pausing/unpausing them on YouTube.)
- Get a list of potential transcription errors that the human reviewer should check for. Copy and paste the Whisper transcript into ChatGPT with the following prompt: *The following is the machine-produced .srt transcrption of a PyCon conference talk. Identify any terms that could have likely been incorrectly transcribed, especially proper names, acronyms, or technical jargon:*
- Tell ChatGPT "More" to provide more possible errors. Repeat this until ChatGPT stops giving useful suggestions.
- Copy and paste this into a file with a name like `pytexas-2024/human-reviewer-notes/talk-name.txt`.
- Using these notes, read through the transcription and make needed corrections. If there are many errors, you may need to play the original talk video (on 2x speed) while reading along to get context, or look up talk info to get things like the correct spelling of the speaker's name.
- Use [https://trends.google.com/](https://trends.google.com/) if you need to determine which term or spelling is more popular. For example, I needed to compare if "foot gun" or "footgun" was the more popular term.
- Commit the corrected .srt transcript as, for example, `pytexas-2024/talk-name.srt`. (We'll use the existence of this file in the repo as a sign that it is finished. Please don't commit half-finished .srt files.) DO NOT CHANGE THE ORIGINAL SRT FILE IN THE `pytexas-2024/originals` FOLDER. COMMIT A NEW FILE.
- Send the videos to the YouTube channel owner so they can add them to the video.

In the future, we'll be adding these transcripts to the PyVideo repo so that they can be searchable on that site. We'll also create translations of these subtitles to non-English languages.

Random Notes
==============


- My finaly conclusion after trying to do human review of a couple of these videos is that it's infeasible to provide human review. Realistically, one hour of talk requires three hours of human work (even watching the talk on 1.5x speed. It's just not a one-to-one kind of task. And this is for the transcripts that are 99% correct already.) We're going to have to rely on machine transcribing, a quick skim for quality, and if the transcriptions aren't high quality, then we just can't publish them. They take too long to fix.
- Pyvideo should have the srt of the original machine transcript, the srt of the human corrections, "todo" notes by the human reviewer for other human reviewers if it isn't done, and the plain text format we put on the site is generated from the srt files. We want to preserve the original machine transcription and we want human editing done to an srt data rather than try to keep srt and text data in sync with each other.
- One question I need to answer: Do any PyCon events already have improved subtitles? (All I've found so far are either YouTube's autogenerated subtitles or no subtitles at all.)
- We should make a priority list based on most popular youtube videos first. This doesn't have to be automated: just make a best guess for popular events (PyCon US is more popular than regional pycons) and views (just look at the playlist and note the relatively popular ones.) Keep it simple.
- Whisper tends to make a "best guess" when it comes to transcriptions, and it will sometimes invent entire sentences that are grammatically correct but completely wrong. This especially happens with speakers who have accents.
- Whisper's transcription quality also drops dramatically for parts where the audio isn't clear, like when the speaker doesn't speak into the microphone or when the audience asks a question not into microphone.
- The speaker's slides in the video have important context for the speaker's names, company names, technical terms, and other information that can help you make accurate transcriptions. Don't just listen to the audio.
- Using keyboard shortcuts makes this process MUCH faster. Alt-tab on Windows and Command-Tab on macOS make it easy to switch between windows while you review the video and correct the .srt text. The space key pauses and unpauses the video in VLC Player. The left arrow key rewinds back 10 seconds in VLC PLayer.
- Start reviewing the video by playing it at normal speed. If you are comfortable and there aren't that many corrections, you can then listen to the video at 1.5x or 2x speed. (I recommend 1.5x)
- The pyvideo website should probably have both the original machine-produced srt, the human-reviewed (and publicly posted on the website) subtitles & text, and (not publicly posted) notes for other subtitlers (suggestions for things to add in later, like "There are two speakers here but I didn't label who is talking when" or "not thoroughly human reviewed but the machine transcription seems accurate").
- Let's not let perfect be the enemy of good. Even some slightly incorrect subtitles are good if we carefully marked them as "human review not completed, unofficial subtitle status". We just want something approximate that search engines can crawl.
