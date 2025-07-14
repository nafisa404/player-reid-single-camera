from sort import Sort

class Tracker:
    def __init__(self):
        self.tracker = Sort()  # Simple Online Realtime Tracking

    def update(self, detections):
        return self.tracker.update(detections)
