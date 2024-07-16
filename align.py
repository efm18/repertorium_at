import os

def combinar_fragmentos(letras_lines, musica_lines):    
    resultado_final = []
    for letras, musica in zip(letras_lines, musica_lines):
        letras_lista = letras.strip().split(" ")
        musica_lista = musica.strip().split(" ")
        
        resultado_linea = []
        for i in range(max(len(letras_lista), len(musica_lista))):
            letra = letras_lista[i] if i < len(letras_lista) else ""
            musica = musica_lista[i] if i < len(musica_lista) else ""
            if letra:
                resultado_linea.append(f"({musica}){letra}")
            else:
                resultado_linea.append(f"({musica})")
        
        resultado_final.append("".join(resultado_linea))
    
    return resultado_final

def process_transcriptions(lyrics_dir, music_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    lyrics_files = sorted(os.listdir(lyrics_dir))
    music_files = sorted(os.listdir(music_dir))
    
    if len(lyrics_files) != len(music_files):
        print("Number of lyrics transcription does not match number of music transcription")
    
    for lyrics_file in lyrics_files:
        music_file = lyrics_file  # Assuming the files have the same name in both directories
        
        lyrics_path = os.path.join(lyrics_dir, lyrics_file)
        music_path = os.path.join(music_dir, music_file)
        
        if os.path.exists(music_path):
            with open(lyrics_path, 'r', encoding='utf-8') as letras_file, open(music_path, 'r', encoding='utf-8') as musica_file:
                letras_lines = letras_file.readlines()
                musica_lines = musica_file.readlines()
            
            resultado_final = combinar_fragmentos(letras_lines, musica_lines)
            
            output_path = os.path.join(output_dir, lyrics_file)
            with open(output_path, 'w', encoding='utf-8') as combined_file:
                for linea in resultado_final:
                    combined_file.write(f"{linea}\n")
        else:
            print(f"Music file for {lyrics_file} not found in {music_dir}")

if __name__ == "__main__":
    lyrics_dir = "predictions/lyrics"
    music_dir = "predictions/music"
    output_dir = "predictions/aligned"
    
    process_transcriptions(lyrics_dir, music_dir, output_dir)