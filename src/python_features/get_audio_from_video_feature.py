# moviepy - библиотека для извлечения звуковой дорожки из видео-файла.

import moviepy.editor as mp

file_path = 'Путь к директории'
# Указываем mp4 файл, из которого будем извлекать звук
clip = mp.VideoFileClip('video_file.mp4', file_path)
# Извлекаем аудио дорожку из видео-файла
clip.audio.write_audiofile('audio_file.mp3')

# Result: в указанной директории будет создан аудио-файл
