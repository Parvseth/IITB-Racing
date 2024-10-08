import cv2
import numpy as np


img = cv2.imread("/home/parv/Desktop/DRIVERLESS/perception")       # load image
cv2.imshow(img)

# assuming 1280x720 for this example
img_height, img_width, _ = img.shape

# Bounding box data
box = [
    [2.0, [0.43476563692092896, 0.7194444537162781, 0.03984374925494194, 0.1111111119389534], 0.8438236117362976],
    [2.0, [0.47539061307907104, 0.737500011920929, 0.04296875, 0.11666666716337204], 0.8504939675331116],
    [0.0, [0.33671873807907104, 0.7111111283302307, 0.03593749925494194, 0.09444444626569748], 0.9057255387306213],
    [3.0, [0.2679687440395355, 0.7361111044883728, 0.04374999925494194, 0.125], 0.919158935546875],
    [0.0, [0.21054688096046448, 0.7479166388511658, 0.04921875149011612, 0.12638889253139496], 0.9196999073028564],
    [3.0, [0.38945311307907104, 0.7201389074325562, 0.03984374925494194, 0.10972221940755844], 0.9205850958824158],
    [3.0, [0.5414062738418579, 0.762499988079071, 0.05312500149011612, 0.14444445073604584], 0.9242506623268127],
    [0.0, [0.610156238079071, 0.7909722328186035, 0.06406249850988388, 0.1736111044883728], 0.9282561540603638]
]

# Draw bounding boxes
for b in box:
    class_id, bbox, confidence = b
    x_center, y_center, width, height = bbox

    # Convert normalized coordinates to pixel coordinates
    x_center *= img_width
    y_center *= img_height
    width *= img_width
    height *= img_height

    # Calculate start and end points of the bounding box
    start_point = (int(x_center - width / 2), int(y_center - height / 2))
    end_point = (int(x_center + width / 2), int(y_center + height / 2))

    
    color = (0, 255, 0)  # Green color for bounding box
    thickness = 2

    
    img = cv2.rectangle(img, start_point, end_point, color, thickness)  # drawing bounding box


cv2.imshow(img)  # display image



