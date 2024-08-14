url ="https://vdept3.bdstatic.com/mda-pg91issmspgww8ac/cae_h264/1688951467835484161/mda-pg91issmspgww8ac.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1723634343-0-0-ee5f0f39420a4d98ebe5b73c631044eb&bcevod_channel=searchbox_feed&pd=1&cr=0&cd=0&pt=3&logid=1143760930&vid=10799492566838649151&klogid=1143760930&abtest="
import requests
response = requests.get(url)
with open("niuBi.mp4", "wb") as f:
    f.write(response.content)
with open("niuBi.mp3", "wb") as g:
    g.write(response.content)
from moviepy.editor import *
Voice_clip = AudioFileClip("niuBi.mp3")
Video_clip = VideoFileClip("niuBi.mp4")
Video_clip.audio = Voice_clip
Video_clip.write_videofile("niuBi_voice.mp4")
