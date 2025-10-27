# ros2_joint_recorder

A minimal ROS 2 package to record /joint_states into a CSV file.

## Build
```bash
cd ~/new_ws
colcon build --packages-select ros2_joint_recorder
source install/setup.bash

### CSV format
\`\`\`
t,<joint1>,<joint2>,...
0.04,1.0,2.0
\`\`\`

## License
MIT
