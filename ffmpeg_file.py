import os
import shutil
import numpy as np
from moviepy.editor import VideoFileClip
from PIL import Image

def create_dirs():
  os.makedirs('./DataEngineeringCourse/ffmpeg_assignment',exist_ok=True)
  base_dir = os.path.abspath('./DataEngineeringCourse/ffmpeg_assignment')
  os.makedirs(os.path.join(base_dir,'Video_input'),exist_ok=True)
  os.makedirs(os.path.join(base_dir,'OutPuts'),exist_ok=True)
  os.makedirs(os.path.join(base_dir,'organized_outs'),exist_ok=True)
  os.makedirs(os.path.join(base_dir,'Output_Samples'),exist_ok=True)
  print('Directories created')



base_dir = os.path.abspath('./DataEngineeringCourse/ffmpeg_assignment')
input_dir = os.path.join(base_dir, 'Video_input')
output_dir = os.path.join(base_dir, 'OutPuts')
organized_dir = os.path.join(base_dir, 'organized_outs')

def get_frames(clp):
  '''
  Gets all Frames from video and saves them in output_dir
  '''
  os.makedirs(os.path.join(output_dir,'All_Frames'),exist_ok=True)
  clip = VideoFileClip(clp)
  for i in range(int(clip.reader.nframes)+1):
    try:
      img = Image.fromarray(clip.get_frame(i))
      img.save(os.path.join(output_dir+'/All_Frames',f'{i}.png'))
    except Exception as e:
      with open(os.path.join(output_dir,'logs.txt'),'a') as f:
        f.write(f'{e} in image {i}\n ')


def organize_frames(fsize):
  all_images = np.array(os.listdir(os.path.join(output_dir,'All_Frames')))
  images_sorted = np.array(sorted(list(map(lambda x: int(x.split('.')[0]),all_images))))
  print(len(images_sorted))
  x = 1
  y = 1
  for i in range(len(images_sorted)-1):
    try:
      os.makedirs(os.path.join(organized_dir,f'{x}'),exist_ok=True)
      shutil.copy(os.path.join(output_dir,'All_Frames',f'{images_sorted[i]}.png'),os.path.join(organized_dir,f'{x}',f'{i}.png'))
      y += 1
      if y == fsize:
        shutil.copy(os.path.join(output_dir,'All_Frames',f'{images_sorted[i]}.png'),os.path.join(base_dir,f'Output_Samples',f'{i}.png'))
        x += 1
        y = 1
    except Exception as e:
      with open(os.path.join(output_dir,'copyErrors.txt'),'a') as f:
        f.write(f'{e} in image {i}\n ')


create_dirs()
get_frames(target_video)
organize_frames(50)


