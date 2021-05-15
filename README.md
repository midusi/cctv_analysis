# CCTV analysis.

A cctv analysis server to asynchronously analyse videos for objects such as persons or cars in cctv camera feeds.
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction.

Ready to run flask cctv_analysis server .
The server uses KERAS model implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K) and openCV model (dnn module) implementation of YOLOv3

---

## Requirements.

-Python3
-Pip3

## Initial setup for model.

1. Install the PyPi cctv_analysis library:
    $ pip3 install cctv_analysis 
2. Run the server module localy:
    $ python3 -m cctv_analysis.run_server
3. Server runs at http://127.0.0.1:5000/ localy, there are 2 options for excuting the models. Synchronous through the browser or asynchronous through an endpoint.

    3.1 Synchronous: Go to http://127.0.0.1:5000/ in the browser, then use the "seleccionar archivo" button, select the video, once the video is selected click at the "enviar" button, after procesing the video you will be redirected and the output will be shown.
    3.2 asynchronous: To use the resource in a asynchronous way you have to send your post request to de endpoint "/model_request" and you must set up a endpoint in the client server so the data can be sended once is procesed. When you make the request to de server you must send the file and the url+endpoint in the post request with this format. 
    
    e.g:

    datas = {'urlCliente' : 'http://127.0.0.1:5001/client_response'}                        #1
    files = [
        ('file', ('../people3.mp4', open('../people3.mp4', 'rb'), 'application/octet')),    #2
        ('datas', ('datas', json.dumps(datas), 'application/json')),
    ]
    url = 'http://127.0.0.1:5000/model_request' #local url + endpoint
    r = requests.post(url, files=files)

    #1 you have to update the 'urlCLiente' value in datas with your url+endpoint 
    #2 you have to update '../people3.mp4' with the path of your video


