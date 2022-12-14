from django.shortcuts import render

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

from .mediapipe import mp_drawing, mp_drawing_styles, mp_pose, skeleton

from .algorithm import get_direction, get_pushup_ready, get_pushup_status

def index(request):
    return render(request, 'index.html')

def screen(request):
    kind = request.GET.get('health')
    print("HTML에서 넘어온 데이터: ", kind)
    return render(request, 'screen.html', {'kind': kind})

def testweb(request):
    return render(request, 'testweb.html')

def testweb2(request):
    return render(request, 'testweb2.html')

class VideoCamera(object):
    def __init__(self, kind):
            self.kind = kind
            self.status = 'none'
            self.dir = 'none'
            self.ready = 'notready'
            self.degree = 'none'
            self.count = 0
            self.video = cv2.VideoCapture(0)
            (self.grabbed, self.frame) = self.video.read()
            threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # image = self.frame
        # image = mpi_keypoint(image, net)
        image, results = skeleton(self.frame, mp_drawing, mp_drawing_styles, mp_pose)
        if self.kind == 'pushup':
            try:
                self.dir = get_direction(results, mp_pose)
                self.ready = get_pushup_ready(results, mp_pose, self.dir)

                if self.ready == 'ready':
                    status, self.degree = get_pushup_status(results, mp_pose, self.dir)
                    if self.status == 'down' and status == 'up':
                        self.count += 1
                    self.status = status
                
                else:
                    self.status = 'none'
                    self.count = 0
                
                # cv2.putText(image, str(self.kind), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
                # cv2.putText(image, str(self.count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)

            except:
                pass
        
        # cv2.putText(image, str(self.count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        # cv2.putText(image, self.dir, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        # cv2.putText(image, self.ready, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        # cv2.putText(image, self.status, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        # cv2.putText(image, str(self.degree), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        # print(self.kind)
        cv2.putText(image, self.kind, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)
        cv2.putText(image, str(self.count), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, lineType=cv2.LINE_AA)

        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def detectme(request):
    try:
        # kind = request.GET.get('health')
        # print(f'detectme로 넘어온 데이터:{kind}')

        kind = 'pushup'
        cam = VideoCamera(kind)
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass