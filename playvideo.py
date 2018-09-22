#Author Zezhong Wang

import subprocess
import os

#Use sbuprocess command to generate a video through ffmpeg
print('before export the vedio')

subprocess.call('ffmpeg -framerate 1/5 -f image2 -i ./images/tpic%d.jpg -crf 25 -pix_fmt yuv420p out.mp4')
print('finish converting vedio')
