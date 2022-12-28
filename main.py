import time

import cv2

# url = "rtsp://root:160track@192.168.1.91/axis-media/media.amp"
url = "rtsp://127.0.0.1:8554/axis-media/media.amp"
out_file = "C:/Users/racoon/PycharmProjects/rtsp/output.mp4"


def read_cap(cap, out = None):
    while cap.isOpened():
        ret, frame = cap.read()

        print(type(frame), ret)

        if frame is None:
            break

        if out is not None:
            out.write(frame)

        frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def capture_cv2():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter(out_file, fourcc, 25.0, (3840, 2160))

    while True:
        try:
            print(f"start capture from {url}")
            cap = cv2.VideoCapture(url)

            read_cap(cap)

            cap.release()
            cv2.destroyAllWindows()

        # except ctrl+c
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

    # out.release()


if __name__ == "__main__":
    capture_cv2()
