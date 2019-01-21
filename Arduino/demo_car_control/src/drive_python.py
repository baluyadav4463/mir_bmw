import rospy
from std_msgs.msg import UInt16
from sensor_msgs.msg import Joy

x = 0
def controller_callback(data):
    control_pub = rospy.Publisher('/Control', UInt16, queue_size = 1)
    rate = rospy.Rate(10)
    x = UInt16()
    if(data.buttons[7] == 1.0):
        print('forward')
        x=8
    if(data.buttons[6] == 1.0):
        print('backward')
        x=2
    if(data.axes[4] == -1.0):
        print('right')
        x=6
    if(data.axes[5] == -1.0):
        print('Extreme_right')
        x=3
    if(data.axes[5] == 1.0):
        print('Extreme_left')
        x=1
    if(data.axes[4] == 1.0):
        print('left')
        x=4
    if(data.buttons[2] == 1.0):
        print('increase_speed')
        x=5
    if(data.buttons[3] == 1.0):
        print('reset')
        x=7
    if(data.buttons[0] == 1.0):
        print('decrease_speed')
        x=9
    #control_data = x
    control_pub.publish(x)
    
def main():
    rospy.init_node('controller_python')
    rospy.Subscriber('/joy', Joy, controller_callback)
    rospy.spin()

if __name__=='__main__':
    main()
