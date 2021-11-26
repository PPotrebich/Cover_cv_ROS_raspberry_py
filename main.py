import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


rospy.init_node('computer_vision_sample')
bridge = CvBridge()

image_pub = rospy.Publisher('~pasha', Image)

def image_callback(data):
    print(".")
    print("'_|_'")
    image = bridge.imgmsg_to_cv2(data, 'bgr8')
    # Do any image processing with cv2...
    # image = cv.circle(image, (100, 100), 10, (0, 0, 255), -1)
    image_pub.publish(bridge.cv2_to_imgmsg(image, 'bgr8'))

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)

rospy.spin()