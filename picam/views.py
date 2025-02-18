from django.shortcuts import render
from django.http import JsonResponse
import paho.mqtt.client as mqtt
import base64
import cv2
import numpy as np
import threading

# MQTT 브로커 정보
MQTT_BROKER = "192.168.0.44"
MQTT_PORT = 1883
MQTT_TOPICS = ["rpi/pi_cam", "rpi/rpi1_cam"]  # 여러 개의 토픽 등록

# 글로벌 변수로 각 라즈베리파이의 최신 프레임 저장
frames = {}

def on_message(client, userdata, msg):
    global frames
    device_id = msg.topic.split("/")[-1]
    image_data = base64.b64decode(msg.payload)
    np_array = np.frombuffer(image_data, dtype=np.uint8)
    frame = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)  # 변경

    frames[device_id] = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode('utf-8')

def mqtt_subscribe():
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

    for topic in MQTT_TOPICS:
        mqtt_client.subscribe(topic, qos=0)

    mqtt_client.loop_start()

# MQTT Subscribe를 백그라운드 스레드에서 실행
mqtt_thread = threading.Thread(target=mqtt_subscribe, daemon=True)
mqtt_thread.start()

def picam(request):
    """ 웹페이지 렌더링 """
    return render(request, 'picam/picam2.html')

def picam_data(request):
    """ JSON 형식으로 실시간 프레임 데이터 반환 """
    return JsonResponse({"frames": frames}, safe=False)



def webcam(request):
    return render(request, 'picam/webcam.html')


