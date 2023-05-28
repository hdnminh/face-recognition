import sys
 
# setting path
sys.path.append('../')

from main import FaceSurveillanceCore


core = FaceSurveillanceCore()


core.process_single_video("3.mp4")



