# Automatic Transcription for Repertorium Project

This repository is designed to perform automatic transcription of the systems from the Repertorium project.

## Directory Structure

Ensure your data is in `.png` format and saved in the `data` directory within the appropriate subdirectory:

- `data/Repertorium_Images_lyrics` for lyrics
- `data/Repertorium_Images_music` for music

## Usage

Once the data is placed in the corresponding folders, execute the command `.run/sh` with one of the following arguments, depending on the desired task:

- `./run.sh music` for transcribing only the files in the `Repertorium_Images_music` directory
- `./run.sh lyrics` for transcribing only the files in the `Repertorium_Images_lyrics` directory
- `./run.sh all` for transcribing the files in both directories and aligning them

## Output

The resulting transcriptions will be saved in the `predictions` directory within their respective subdirectories:

- `predictions/music` for music transcriptions
- `predictions/lyrics` for lyrics transcriptions
- `predictions/aligned` for aligned transcriptions

> **Note:** The models are still in development.
