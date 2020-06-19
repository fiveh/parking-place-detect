import cv2
import time
from async_stream import VideoCaptureAsync
from Xlib import display, X
from PIL import Image  #PIL
# from new.number_recognizer_rcnn import NumberRecognizerRCNN

def get_image():
    W,H = 900,800
    dsp = display.Display()
    root = dsp.screen().root
    raw = root.get_image(0, 240, W,H, X.ZPixmap, 0xffffffff)
    image = Image.frombytes("RGB", (W, H), raw.data, "raw", "RGBX")

    return image




def test(n_frames=500, async=False):
    cap = VideoCaptureAsync(0)
    cap.start()
    # t0 = time.time()
    i = 0
    # while i < n_frames:
    while True:
        _, frame = cap.read()
        cv2.imshow('Frame', frame)
        # i += 1
        if cv2.waitKey(1) == ord('q'):
            break
        print(i)
    # print('[i] Frames per second: {:.2f}, async={}'.format(n_frames / (time.time() - t0), async))
    cap.stop()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # test(n_frames=300, async=True)
    img = cv2.imread('aa.bmp')
    cv2.imwrite('oo.jpg',img)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)