import cv2

class Sketch(object):

    def _sketch(self, image):

        # Converting the image to grayscale
        grayIm = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Clean up the image using Gaussian Blur
        grayImBlur = cv2.GaussianBlur(grayIm, (5, 5), 0)

        # Extracting the edges
        cannyEdges = cv2.Canny(grayImBlur, 10, 70)

        # This invert the image binarized
        _, mask = cv2.threshold(cannyEdges, 70, 255, cv2.THRESH_BINARY_INV)

        return mask

    def initWebCan(self):

        # Initialize the webcam and web is the object provided by VideoCapture
        # It contains a boolean indicating if it was successful (ret)
        # And contains the images collected from the webcam (frames)
        web = cv2.VideoCapture(0)

        while (True):

            ret, frame = web.read()
            cv2.imshow("Our Live Sketcher", self._sketch(frame))

            if (cv2.waitKey(1) == 13): # 13 is the Enter Key

                break

        # Release the camera and close the windows
        web.release()
        cv2.destroyAllWindows()

        return