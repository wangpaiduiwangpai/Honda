url = "https://apd-vlive.apdcdn.tc.qq.com/vhot2.qqvideo.tc.qq.com/ABEt7lj3s7xyL5l8l1oBJEPwk_73HmNJPBP0hFnzrPmU/B_JxNyiJmktHRgresXhfyMesSz4FAy0xEoqRpuFsOx-05kVumlF01okrbFz1kEIy75/svp_50069/gzc_1000035_0bc3jib7saadjmapxw62dfrzmswd7ffah6ka.f622.mp4?sdtfrom=v1010&guid=a190c31b7a7a9dff&vkey=4FBB872365283E0F2EA09EB45A417C55301B218CA694150E53BC5E1AC7D0B8E11EE30FCCA50D09DAA0B0872EC9EBEC742862237C295E4E98F95FB48F3ECD8446266E1E37FAACBEB0AA7616A41740F04137978FB862935DA86BE31E807F153B4BA0533F0E2876189DD835C348E39500E00C836E788C73167830B605633DB77B3198B52208649440DD3D3BD52FB2A8935CBDC06BE766283095E17D96E7C33036047AC74844D679922C"

import requests
response = requests.get(url)
with open("dameinv.mp4", "wb") as f:
    f.write(response.content)
with open("dameinv.mp3", "wb") as g:
    g.write(response.content)
from moviepy.editor import *
video = VideoFileClip("dameinv.mp4")
audio = AudioFileClip("dameinv.mp3")
final_clip = video.set_audio(audio)
final_clip.write_videofile("dameinv.mp4")











