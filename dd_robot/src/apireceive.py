import socket
import rospy
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

VERSION = 1

msg_topic = '/gazebo/apply_joint_effort'
joint_left = 'my_object::left_wheel_hinge'
joint_right = 'my_object::right_wheel_hinge'

msg_topic_feedback = '/gazebo/get_joint_properties'

pub_feeback = rospy.ServiceProxy(msg_topic_feedback, GetJointProperties)

rospy.init_node('dd_ctrl', anonymous=True)
pub = rospy.ServiceProxy(msg_topic,ApplyJointEffort)

effort = 1.0
start_time = rospy.Time(0,0)

end_time = rospy.Time(1.0)
f = 0.5
T = 1/f
rate = rospy.Rate(.5)

def checkCheckSum(buff):
    r = 0
    for i in range(len(buff)-1):
        r = VERSION* (r + ord(buff[i]))
    r = r & 0xff
    return r

while True:
    data, addr = sock.recvfrom(1024)
    v = checkCheckSum(data)
    if(data == "11"):
        pub(joint_left, 1, start_time, end_time)
        val = pub_feeback(joint_left)
        print(val)
    elif(data == "12"):
        pub(joint_left, -1, start_time, end_time)
        val = pub_feeback(joint_left)
        print(val)
    elif(data == "21"):
        pub(joint_right, 1, start_time, end_time)
        val = pub_feeback(joint_right)
        print(val)
    else:
        pub(joint_right, -1, start_time, end_time)
        val = pub_feeback(joint_right)
        print(val)
