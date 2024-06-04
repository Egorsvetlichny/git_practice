# moviepy - библиотека для извлечения звуковой дорожки из видео-файла.

from moviepy.editor import VideoFileClip

file_path = r'C:\Users\Алина\Downloads\Telegram Desktop\video.mp4'

# Указываем mp4 файл, из которого будем извлекать звук
video_clip = VideoFileClip(file_path)

# Извлекаем аудио дорожку из видео-файла
audio_clip = video_clip.audio.write_audiofile('audio_file.mp3')

# Закрытие видео и аудио клипов
video_clip.close()
audio_clip.close()

# Result: в указанной директории будет создан аудио-файл
