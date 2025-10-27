# ros2_joint_recorder

A minimal ROS 2 package to record `/joint_states` into a CSV file.
---

## 🚀 Quick Start

```bash
# clone the repo
git clone git@github.com:LDWLDWLDW666/ros2_joint_recorder.git
cd ros2_joint_recorder

# build
colcon build --packages-select ros2_joint_recorder
source install/setup.bash

# run
ros2 run ros2_joint_recorder joint_recorder --ros-args \
  -p topic:=/joint_states -p out:=/tmp/joint_log.csv
````

Stop with `Ctrl+C`.
The CSV will be saved at `/tmp/joint_log.csv`.

---

## 📄 CSV format

```
t,<joint1>,<joint2>,...
0.04,1.0,2.0
```

---

## 🪪 License
```
MIT
```
