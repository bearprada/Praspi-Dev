import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO

isFlashmode = False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("index.html")

class BaseHandler(tornado.web.RequestHandler):
    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

class OnOpHandler(BaseHandler):
    def get(self):
        self.setup()
        #isFlashmode = True
        GPIO.output(7, GPIO.LOW)
        self.write("on it")

class OffOpHandler(BaseHandler):
    def get(self):
        self.setup()
        #isFlashmode = False
        GPIO.output(7, GPIO.HIGH)
        self.write("off it")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/on", OnOpHandler),
    (r"/off", OffOpHandler)
])

def myfunc(i):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    while True :
        print str(isFlashmode)
        if isFlashmode == True:
            GPIO.output(7, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(7, GPIO.LOW)
            time.sleep(1)

if __name__ == "__main__":
    application.listen(8080,'0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()
    #t = Thread(target=myfunc, args=(0,))
    #time.sleep(1)
    #t.start()
