from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pytesseract
import cv2
from moviepy.editor import *
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\pk202\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


def readFromLrc(filePath):
    with open(filePath, 'r') as f:
        song = f.read()
    return song


def editVid(videoPath):
    clip = (VideoFileClip(videoPath)
        .fx( vfx.colorx, 0.5))
    clip.write_videofile('videoAfterEdit.mp4',fps=25,codec='mpeg4')





def writeOnImg(backgroundImgPath, stringToWrite, outputFile):

    img = Image.open(backgroundImgPath)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("fonts/OpenSans-ExtraBoldItalic.ttf", int(height/20))
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text(( width/10, height/5), stringToWrite, (255, 255, 255), font=font)
    img.save(outputFile)


def extractFrames(pathIn, pathOut, fps=1):
    ''' Given video it will extract the frames.
    pathIn: path to the video.
    pathOut: path where frames are to be stored.
    fps. frames per second. 1 initially '''
    try:
        count = 1
        vidcap = cv2.VideoCapture(pathIn)
        success = True
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*1000)/fps)    # added this line
            success, image = vidcap.read()
            cv2.imwrite(os.path.join(pathOut + "{}.jpg".format(count)), image)     # save frame as JPEG file
            count = count + 1
    except Exception as e:
        print(e)
    return count

# editVid('videoForEdit.mp4')
nframes = extractFrames('Waka.mp4', 'frames/')

for x in range(1, nframes):
    textt = image_to_string(Image.open('frames/' + str(x) + '.jpg'), lang='eng')
    writeOnImg(backgroundImgPath='pic_for_video/picvid6.jpg', stringToWrite = textt, outputFile='output_frames/' + str(x) + '.jpg')

