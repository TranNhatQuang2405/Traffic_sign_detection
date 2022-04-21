import cv2
from utils import get_localization_label
import time


def main():
    video = 'http://192.168.136.194:4747/video'
    cap = cv2.VideoCapture(video)
    frame_number = 0
    generate_img = True
    save_path = "./images/demo"
    print(save_path)
    order_list = ["speed_10", "speed_30", "speed_80",
                  "turn_left", "turn_right", "stop", "do_nothing", "None"]

    while True:
        _, frame = cap.read()
        try:
            sign, sign_type, coordinate = get_localization_label(frame)

            box_fra = frame.copy()
            if coordinate:
                cv2.rectangle(box_fra, coordinate[0],
                              coordinate[1], (0, 255, 0), 2)
                if generate_img:
                    sav_img = cv2.resize(
                        sign, (32, 32), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(save_path + "%04d" %
                                frame_number + '_' + order_list[int(sign_type)]+".png", sav_img)

            # operate(int(sign_type))
            print("Order:[", sign_type, "]", order_list[int(sign_type)])
            cv2.imshow("Real-time scene", box_fra)

        except:
            print("error")

        k = cv2.waitKey(1)

        if k == 27:
            break

        elif k == ord("s"):
            cv2.imwrite(".\\images\\capture\\capture_%04d_%s" %
                        frame_number + '_' + order_list[int(sign_type)]+".png", frame)

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()


main()
