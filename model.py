import os

def detect_pothole(img_path):
    os.system("cd darknet && ./darknet detector test data/obj.data cfg/yolov4-custom.cfg \
              ../model/yolov4-custom_best.weights .{} -thresh 0.3 -dont_show -map".format(img_path))