# Automatic Transcription for Repertorium Project

This repository is designed to perform automatic transcription of the systems from the Repertorium project.

## Directory Structure

Ensure your data is in `.png` format and saved in the `data` directory within the appropriate subdirectory:

- `data/Repertorium_Images_lyrics` for lyrics
- `data/Repertorium_Images_music` for music
- `data/Repertorium_Images_full` for aligned transcription

## Usage

Firstly, you need to execute the following commands in order to build and run the docker (**it is needed an linux/amd64 system with cuda**):
- `./build_docker.sh`
- `./run_docker.sh`

Once the data is placed in the corresponding folders and you are inside the docker container, execute the command `.transcribe/sh` with one of the following arguments, depending on the desired task:

- `./transcribe.sh music` for transcribing only the files in the `Repertorium_Images_music` directory
- `./transcribe.sh lyrics` for transcribing only the files in the `Repertorium_Images_lyrics` directory
- `./transcribe.sh aligned` for transcribing the files in the `Repertorium_Images_full` directory

## Output

The resulting transcriptions will be saved in the `predictions` directory within their respective subdirectories:

- `predictions/music` for music transcriptions
- `predictions/lyrics` for lyrics transcriptions
- `predictions/aligned` for aligned transcriptions

> **Note:** The models are still in development.
