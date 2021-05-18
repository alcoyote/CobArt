from ImageProcessing.blur import Blur
from ImageProcessing.edge_detection import EdgeDetection
from ImageProcessing.morphology import Morphology
from ImageProcessing.sharpening_with_kernel import SharpeningWithKernel


class ImageProcess:
    def __init__(self):
        self.image = None
        self.original_image = None
        self.temp_images = []
        self.blur = Blur()
        self.kernel = SharpeningWithKernel()
        self.edge_detection = EdgeDetection()
        self.morphology = Morphology()
