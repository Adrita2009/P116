import cv2

img = cv2.imread("solar-system.jpeg")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            44,
            (255,255,255)
            )