from ImageProcessing.blur import Blur
from ImageProcessing.edge_detection import EdgeDetection
from ImageProcessing.morphology import Morphology
from ImageProcessing.kernel import Kernel


class ImageProcess:
    def __init__(self):
        self.image = None
        self.original_image = None
        self.temp_images = []
        self.blur = Blur()
        self.kernel = Kernel()
        self.edge_detection = EdgeDetection()
        self.morphology = Morphology()
