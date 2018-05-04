# coding: utf-8

import numpy as np
import cv2
import sys
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame
from pylibfreenect2 import createConsoleLogger, setGlobalLogger
from pylibfreenect2 import LoggerLevel
import time
import os

try:
    from pylibfreenect2 import OpenCLPacketPipeline
    pipeline = OpenCLPacketPipeline()
except:
    try:
        from pylibfreenect2 import OpenGLPacketPipeline
        pipeline = OpenGLPacketPipeline()
    except:
        from pylibfreenect2 import CpuPacketPipeline
        pipeline = CpuPacketPipeline()
print("Packet pipeline:", type(pipeline).__name__)

# Create and set logger
logger = createConsoleLogger(LoggerLevel.Debug)
setGlobalLogger(logger)

fn = Freenect2()
num_devices = fn.enumerateDevices()
if num_devices == 0:
    print("No device connected!")
    sys.exit(1)

serial = fn.getDeviceSerialNumber(0)
device = fn.openDevice(serial, pipeline=pipeline)

listener = SyncMultiFrameListener(
    FrameType.Color | FrameType.Ir | FrameType.Depth)

# Register listeners
device.setColorFrameListener(listener)
device.setIrAndDepthFrameListener(listener)

device.start()

# NOTE: must be called after device.start()
registration = Registration(device.getIrCameraParams(),
                            device.getColorCameraParams())

undistorted = Frame(512, 424, 4)
registered = Frame(512, 424, 4)

# Optinal parameters for registration
# set True if you need
need_bigdepth = False
need_color_depth_map = False

bigdepth = Frame(1920, 1082, 4) if need_bigdepth else None
color_depth_map = np.zeros((424, 512),  np.int32).ravel() \
    if need_color_depth_map else None

###################################################################
###################################################################
######################   add new txt file  ########################
action_class = 2
name = 'hj'

###################################################################
###################################################################
loop = 10

for loop in range(loop):
	f = open("action_{}.txt".format(action_class),"r")
	n_collection = int(f.read())
	f.close()


	frame_num = 1
	res_x = int(1920 / 3) 
	res_y = int(1080 / 3)


	image_dir = os.path.join('/media/lsc/New Volume/Data/Action_data', 'action_' + str(action_class), name + 
		                                                '_' + str('{:04d}'.format(n_collection)))


	if not os.path.exists(image_dir):
	    os.makedirs(image_dir)

	print('''




			##########################################
			#       ##                  ###          #
			#                                        #
			#                                        #
			#                                        #
			#                                        #
			#          ##             ##             #
			#                                        #
			#                 ##                     #
			#                ##                      #
			##########################################



	                                                   


	                                                    ''')

	time.sleep(4)



	time.sleep(1)
	print('''                                                    



	                                                    

	 ###############################################################################






	                                                    ''')

	time.sleep(1)
	print('''                                                    




	
	###############################################################################
	###############################################################################



	                                                   


	                                                    ''')


	time.sleep(1)
	print('''                                                    

	 █   ____________________________________________________________________     ▐▌
	 █  /\                                                                   \    ▐▌
	 █  \_|        /\          /\          /\          /\          /\        |    ▐▌
	 █    |     /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\     |    ▐▌
	 █    |  /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\  |    ▐▌
	 █    | //\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\ |    ▐▌
	 █    | \\//\/          ,                                         \/\\// |    ▐▌
	 █    |  \/         /\^/`\                                           \/  |    ▐▌
	 █    |  /\        | \/   |    ________________                      /\  |    ▐▌
	 █    | //\\       | |    |   ( mewbies.com    )          jgs       //\\ |    ▐▌
	 █    | \\//       \ \    /   ( examples of    )        _ _         \\// |    ▐▌
	 █    |  \/         '\\//'    ( boxes command  )      _{ ' }_        \/  |    ▐▌
	 █    |  /\           ||      ( line for linux )     { `.!.` }       /\  |    ▐▌
	 █    | //\\          ||       ----------------      ',_/Y\_,'      //\\ |    ▐▌
	 █    | \\//          ||  ,          o   ,__,          {_,_}        \\// |    ▐▌
	 █    |  \/       |\  ||  |\          o  (O~)____        |           \/  |    ▐▌
	 █    |  /\       | | ||  | |            (__)    )\    (\|  /)       /\  |    ▐▌
	 █    | //\\      | | || / /              U||--|| *     \| //       //\\ |    ▐▌
	 █    | \\//       \ \||/ /                              |//        \\// |    ▐▌
	 █    |  \/         `\\//`   \   \./    \\   \./    \ \\ |/ /        \/  |    ▐▌
	 █    |  /\        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       /\  |    ▐▌
	 █    | //\\/\                                                    /\//\\ |    ▐▌
	 █    | \\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\// |    ▐▌
	 █    |  \/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/  |    ▐▌
	 █    |     \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/     |    ▐▌
	 █    |        \/          \/          \/          \/          \/        |    ▐▌
	 █    |   _______________________________________________________________|_   ▐▌
	 █     \_/_________________________________________________________________/  ▐▌
	     ''')

	time.sleep(0.2)

	start = time.time()

	end = time.time()

	while (end - start) < 3:
	# while True:
	    frames = listener.waitForNewFrame()

	    color = frames["color"]
	    ir = frames["ir"]
	    depth = frames["depth"]

	    registration.apply(color, depth, undistorted, registered,
	                       bigdepth=bigdepth,
	                       color_depth_map=color_depth_map)

	    # NOTE for visualization:
	    # cv2.imshow without OpenGL backend seems to be quite slow to draw all
	    # things below. Try commenting out some imshow if you don't have a fast
	    # visualization backend.
	         
	    cv2.imshow("color", cv2.resize(color.asarray(), 
	    	                           (res_x, res_y)))
	    
	    
	    cv2.imwrite(os.path.join(image_dir, 'color_' + 'action_' + str(action_class) + '_num_' + str('{:04d}'.format(n_collection)) + '_' +
	    	                           str('{:04d}'.format(frame_num)) + '.jpg'), cv2.resize(color.asarray(),
	                                   (res_x, res_y)))
	    
	    frame_num += 1

	    end = time.time()

	    listener.release(frames)

	    key = cv2.waitKey(delay=1)
	    if key == ord('q'):
	        break

	n_collection += 1
	f = open("action_{}.txt".format(action_class),'w')
	f.write(str(n_collection))
	f.close()




device.stop()
device.close()

sys.exit(0)
