from app import fun

from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my key"


@app.route('/')
def index():
    flash("Video Been Streaming")
    return render_template('frame.html')


@app.route('/video')
def video():
    # x= fun()
    # a = next(x)
    # b = next(x)

    return Response(fun(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video1')
def video1():
    return Response(next(next(fun())), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_dup')
def video_dup():
    return render_template('stream.html')


# def paint():
#     return Response(fun(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/vedio')
# def video():
#     return Response(fun(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/button")
def button():
    return "Start"


if __name__ == '__main__':
    app.run(debug=True)
