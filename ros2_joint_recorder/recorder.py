import os, csv, time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class Recorder(Node):
    def __init__(self):
        super().__init__('joint_recorder')
        self.declare_parameter('topic', '/joint_states')
        self.declare_parameter('out', 'joint_log.csv')
        topic = self.get_parameter('topic').get_parameter_value().string_value
        out_path = self.get_parameter('out').get_parameter_value().string_value
        os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
        self._out = open(out_path, 'w', newline='')
        self._writer = csv.writer(self._out)
        self._names = None
        self._t0 = time.monotonic()
        self.create_subscription(JointState, topic, self.cb, 10)
        self.get_logger().info(f"Recording {topic} -> {out_path} (Ctrl+C to stop)")

    def cb(self, msg: JointState):
        if self._names is None:
            self._names = list(msg.name)
            self._writer.writerow(['t'] + self._names)
        name2pos = dict(zip(msg.name, msg.position))
        row = [time.monotonic() - self._t0] + [name2pos.get(n, '') for n in self._names]
        self._writer.writerow(row)

    def destroy_node(self):
        try: self._out.close()
        except Exception: pass
        return super().destroy_node()

def main():
    rclpy.init()
    n = Recorder()
    try:
        rclpy.spin(n)
    except KeyboardInterrupt:
        pass
    n.destroy_node()
    try:
        rclpy.shutdown()
    except Exception:
        pass
