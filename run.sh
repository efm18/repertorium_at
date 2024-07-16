if [ "$1" = "lyrics" ]; then
    python -u transcribe.py --ds_name lyrics --checkpoint_path weights/repertorium_lyrics_char_crnn_greedy.ckpt
elif [ "$1" = "music" ]; then
    python -u transcribe.py --ds_name music --checkpoint_path weights/repertorium_music_char_crnn_greedy.ckpt
elif [ "$1" = "all" ]; then
    python -u transcribe.py --ds_name lyrics --checkpoint_path weights/repertorium_lyrics_char_crnn_greedy.ckpt
    python -u transcribe.py --ds_name music --checkpoint_path weights/repertorium_music_char_crnn_greedy.ckpt
    python -u align.py
else
    echo "Usage: $0 {lyrics|music|all}"
    exit 1
fi