#include <ros/ros.h>
#include <std_msgs/UInt16.h>
#include <iostream>
#include <sensor_msgs/Joy.h>

void controller_callback(const sensor_msgs::Joy::ConstPtr& joy){
int x=0;
std_msgs::UInt16 msg;
ros::NodeHandle n;
 ros::Publisher Control_pub = n.advertise<std_msgs::UInt16>("Control", 1000);
        if(joy->buttons[7]==1.0){
        ROS_INFO("forward");
        x=8;
        }
        if(joy->buttons[6]==1.0){
        ROS_INFO("backward");
        x=2;
        }

        if(joy->axes[4]==-1.0){
        ROS_INFO("Right");
        x=6;
        }
        if(joy->axes[5]==-1.0){
        ROS_INFO("Extreme right");
        x=3;
        }

        if(joy->axes[5]==1.0){
        ROS_INFO("Extreme left");
        x=1;
        }


        if(joy->axes[4]==1.0){
        ROS_INFO("Left");
        x=4;
        }

        if(joy->buttons[2]==1.0){
        ROS_INFO("increase speed");
        x=5;
        }
	if(joy->buttons[3]==1 ){
        ROS_INFO("Reset");
        x=7;
        }
        if(joy->buttons[0]==1.0){
        ROS_INFO("decrease speed");
        x=9;
        }



 msg.data = x;
Control_pub.publish(msg);
 ros::spin();

    }


int main(int argc, char **argv)
{
  int x=0;
  ros::init(argc, argv, "controller");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("joy", 10000, controller_callback);
  ros::spin();
  return 0;
}
