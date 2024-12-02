from PIL import ImageGrab
import easyocr
import numpy

def screen_recognition():
    # 截取屏幕
    screen = ImageGrab.grab()
    # screen.show()
    screen_np = numpy.array(screen)

    # 初始化reader，指定语言
    reader = easyocr.Reader(['ch_sim', 'en'])  # Chinese and English

    # 读取图片
    result = reader.readtext(screen_np)

    # 输出结果
    for (bbox, text, prob) in result:
        print(f"Box: {bbox}, Text: {text}, Probability: {prob}")