import requests, json
import threading
import queue
import websocket
import time
import tkinter as tk

# Tkinter 초기화
window = tk.Tk()
window.title("Ping Tester")

# 핑 결과를 표시할 레이블


def ping_thread():
    url = 'http://localhost:3000/ping'  # 서버의 URL로 변경해야 합니다.
    ping_count = 3
    ping_times = []
    while True:
        for _ in range(ping_count):
            start_time = time.time()
            try:
                response = requests.get(url)
                response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생
                end_time = time.time()
                ping_time = (end_time - start_time) * 1000  # 밀리초로 변환
                ping_times.append(ping_time)
            except Exception as e:
                print(f'Error: {e}')

            time.sleep(1)  # 1초 대기

        average_ping = sum(ping_times) / len(ping_times)
        # ping_label.config(text=f'Average Ping: {average_ping:.2f} ms')
        update_ping_label(average_ping)

def update_ping_label(average_ping):
    ping_label.config(text=f'Average Ping: {average_ping:.2f} ms')


ping_label = tk.Label(window, text='Average Ping: -')
ping_label.pack()

# GUI 업데이트 함수를 호출하여 시작하고 정기적으로 예약합니다.
ping_thread = threading.Thread(target=ping_thread)
ping_thread.daemon = True
ping_thread.start()

window.mainloop()  # Tkinter의 메인 루프 실행





ping_thread = threading.Thread(target=ping_thread)
ping_thread.daemon = True
ping_thread.start()

def start_ping():
    ping_thread.start()

# "Start Ping" 버튼


    

data = {
    'id': 'example',
    'pd':'example1'

}
headers={}
url3='http://127.0.0.1:3000/signin'
url2='http://127.0.0.1:3000/user'

response = requests.post(url3, data=data, headers=headers)
print(response.text)

response_data=json.loads(response.text)
token = {'token':response_data.get('message')}
print('ttttasdasd',token)
response2 = requests.post(url2, json=data, headers=token)
print('dfdsf',response2.text)

data2={
#   'headers':'matching',
#   'id':'ysj',
'token':token

}
data3={
#   'headers':'matching',
#   'id':'ysj',
'headers':'matching'

}
url = f'ws://127.0.0.1:3000'
ws = websocket.create_connection(url)
def data_receive():
    while True:
        data = ws.recv()
        # 받은 데이터 처리
        q.put(data)
            
        print(q.get())
q = queue.Queue()
thread = threading.Thread(target=data_receive, args=())
thread.daemon = True
thread.start()

try:
   
    ws.send(json.dumps(data2))
    data_receive()
    ws.send(json.dumps(data3))
    
except Exception as e:
    print(f'Error: {e}')


# 애플리케이션 실행
window.mainloop()


