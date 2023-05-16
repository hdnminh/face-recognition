import sys
 
# setting path
sys.path.append('../')

from main import FaceSurveillanceCore


core = FaceSurveillanceCore()


core.process_single_video("trinh.mp4")
