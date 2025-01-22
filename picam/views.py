from django.shortcuts import render
import paho.mqtt.client as mqtt
import threading


# Create your views here.

# MQTT 브로커 정보
MQTT_BROKER = "192.168.0.44"
MQTT_PORT = 1883
MQTT_TOPIC = "raspberrypi/camera"

# 글로벌 변수로 프레임 저장
current_frame_base64 = None

def on_message(client, userdata, msg):
    global current_frame_base64
    # MQTT 메시지를 base64로 저장
    current_frame_base64 = msg.payload.decode('utf-8')

def mqtt_subscribe():
    mqtt_client = mqtt.Client()
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.subscribe(MQTT_TOPIC)
    mqtt_client.loop_forever()

# MQTT Subscribe를 백그라운드 스레드에서 실행
mqtt_thread = threading.Thread(target=mqtt_subscribe, daemon=True)
mqtt_thread.start()

def picam(request):
    global current_frame_base64
    return render(request, 'picam/picam.html', {'current_frame_base64': current_frame_base64})
