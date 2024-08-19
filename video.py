url = "https://apd-vlive.apdcdn.tc.qq.com/vhot2.qqvideo.tc.qq.com/AW-UMEJc2jLaeMzA7BXmNWFvs0MOKRKKs8emLvY0tg-w/B_JxNyiJmktHRgresXhfyMet_S2Y45tPPhNhf690EPp36hyBOooaiYOuV26gLdZm3i/svp_50069/gzc_1000035_0bc3saajqaaak4aet2nwljtjlegdtciabgca.f622.mp4?sdtfrom=v1010&guid=a190c31b7a7a9dff&vkey=26E8ECFA107687EB36DD913531BB854AB0973589050CF0F15125D640A3C78E930DF349DD7AECC47E5B54063230C854550DC96A71466803DE218E627DA17F548DEF5B22BB24C47AB6399B2995EE4EEBBF5CD8D12E0357D70D66C77184C700BB1AEE97C1CE3017F0B1C321F7289C9AA5B535BC603D37EB1AA0023514696BD480379B77E35BA375CC4E54A9BF97C1C14675C3BCB75B4B4FF2956E21325D2029776972720E4413397B89"
import requests
response = requests.get(url)
with open("video.mp4", "wb") as f:
    f.write(response.content)
with open("video.mp3", "wb") as k:
    k.write(response.content)
from moviepy.editor import *
Video = VideoFileClip("video.mp4")
Audio = AudioFileClip("video.mp3")
final_clip = Video.set_audio(Audio)
final_clip.write_videofile("神话传说.mp4")



