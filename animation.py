import os, time, sys

frames = []
again = True
delay = 0.15


def animate(frames, times):
  
  for i in range(times):
    for frame in frames:
      os.system('clear')
      print(frame)
      time.sleep(delay)


def writeframes(frames, length, times, delay):
  
  with open('framesdata.txt', 'a') as f:
    framenum = 1
    f.write('\n')
    
    for frame in frames:
      f.write(f"Frame {framenum}: \"{frame}\"")
      f.write('\n')
      framenum += 1
      
    f.write(f'Times Run: {times}, Length: {delay}\n')
    f.write(f'Total length: {length} seconds\n')
    

def getframes():
  global frames
  
  frames = []
  framesnum = int(input('How many frames do you want to generate? '))
  
  for i in range(framesnum):
    frames.append(input('Enter a frame: '))
  return framesnum


def main():
  framesnum = getframes()
  
  delay = input('How long in between frames? (Default is 0.15) ')
  times = int(input("How many times do you want to run the animation? "))
  
  length = float(float(framesnum) * float(delay)) * float(times)
  print('Animation will run for', length,'seconds')
  time.sleep(1)
  
  animate(frames, times)
  writeframes(frames, length, times, delay)
  
  againi = input("Do you want to generate another animation? (y/n) ")

  if againi == "y":
    again = True
  else:
    sys.exit()


while again == True:
  main()
