import threading
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout
import cv2


class CameraApp(App):

    #def __init__(self, **kwargs):
        #super(CameraApp, self).__init__(**kwargs)  # Needed.
    def build(self):

        def exitvid(*args):
            self.stop_vid()
            exit()

        #Vertical Boxlayout for camera and exitButton
        self.camerabox = BoxLayout(orientation='vertical')
        #Videoscreen
        self.vid = Image(allow_stretch=False, keep_ratio=True)
        #Exitbutton
        self.exitButton = Button(text="EXIT", background_color=(1, 0, 1, 1), size_hint=(None, None), size=(Window.width, 100), font_size="30sp", padding=(20, 20))
        #Bind exitbutton to function
        self.exitButton.bind(on_press=exitvid)
        #Adding widgets to box
        self.camerabox.add_widget(self.vid)
        self.camerabox.add_widget(self.exitButton)
        #variable to cut while-loop in runvideo
        self.do_vid = True
        #Starting thread for cv2 capture
        threading.Thread(target=self.runvideo, daemon=True).start()
        #return the camerabox_widget
        return self.camerabox

    #cv2 Capture
    def runvideo(self):
        #Creating named window 'Hidden'
        cv2.namedWindow('Hidden', cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
        #Resizing the window to minimum
        cv2.resizeWindow('Hidden', 0,0)
        #hiding cv2 videowindow in top left screen
        cv2.moveWindow('Hidden',-100,-100)
        #Capturing from source, ex: 'rtsp://username:password@172.0.0.1/live1.sdp'
        cap = cv2.VideoCapture('rtsp://username:password@IP-Address/live1.sdp')
        #cv2-loop
        while (self.do_vid):
            ret, frame = cap.read()
            #initiating display_frame once for each loop
            Clock.schedule_once(partial(self.display_frame, frame))
            cv2.imshow('Hidden', frame)
            cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()

    #stop_while-loop in runvideo()
    def stop_vid(self):
        self.do_vid = False

    #creating texture to send to Image Object.
    def display_frame(self, frame, dt):
        texture = Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(frame.tobytes(order=None), colorfmt='bgr', bufferfmt='ubyte')
        texture.flip_vertical()
        self.exitButton.size[0] = self.vid.size[0]
        self.vid.texture = texture

#Main_Loop
if __name__ == '__main__':
    application = CameraApp()
    Window.fullscreen = False
    application.run()
