# server.py
import asyncio
import json

from fastapi import FastAPI, WebSocket
import uvicorn
from starlette.websockets import WebSocketDisconnect

from pyim import req_get, HOST, assetAndCashFlowChart

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 手动验证WebSocket握手
    if websocket.headers.get("upgrade", "").lower() != "websocket":
        await websocket.close(code=1003)
        return

    await websocket.accept()
    # print("客户端已连接")
    client_ip = websocket.client.host
    print(f"客户端 {client_ip} 已连接")

    try:
        while True:
            try:
                message = await websocket.receive_text()
                print(f"收到来自 {client_ip} 的消息: {message}")

                # 模拟处理延迟
                await asyncio.sleep(0.3)

                if str(message).lower() == 'asset and cash':
                    # TODO: 发送请求给pyim
                    params = {
                        "timeRange": "3",
                        "isPlatform": "1",
                        "inceptionDate": 20230101,
                    }
                    res = req_get(f"{HOST}{assetAndCashFlowChart}", params=params)
                    print(res['data'])
                    response = json.dumps(res['data'])
                else:
                    response = f"{message}"

                await websocket.send_text(response)
            except WebSocketDisconnect:
                print(f"客户端 {client_ip} 主动断开")
                break
            except Exception as e:
                print(f"处理消息时出错: {e}")
                await websocket.close(code=1011)  # 1011表示服务器错误
    except WebSocketDisconnect:
        print(f"客户端主动断开")
    except Exception as e:
        print(f"连接异常: {e}")
    finally:
        await websocket.close()
        print("连接已关闭")


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8008,
        # 重要WebSocket配置
        ws_ping_interval=30,
        ws_ping_timeout=30,
        ws_max_size=10 * 1024 * 1024  # 10MB消息限制
    )