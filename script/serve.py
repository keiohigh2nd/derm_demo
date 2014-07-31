import sift_sh_NBNN_file
import sys, time
import subprocess, os
import draw_file

def calculate_distance():
  p = subprocess.Popen(['g++ -O2 tab.cpp'], shell=True)
  p.wait()
  p = subprocess.Popen(['./a.out'], shell=False)
  p.wait()

def extract_feature_query(img_path):
  sift_sh_NBNN_file.feature_extraction(img_path)

def draw_img(img_path):
  draw_file.draw(img_path)
 
def classify():
  new_img = 'new.jpg'
  extract_feature_query(new_img)
  calculate_distance() 
  draw_img(new_img)

if __name__ == "__main__":
  argvs = sys.argv

  print '--start thread ---'
  for i in range(1000):
    check_new_file()

  #extract_feature_query(argvs[1])
  #calculate_distance() 
  #draw_file(argvs[1])
