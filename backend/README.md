# 拾界乐园 FastAPI 后端

给 uni-app 前端提供登录、盲盒列表、加权抽卡、余额返还和集卡进度接口。开发阶段用 SQLite，验证码固定为 `123456`。

## 启动

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

文档：http://127.0.0.1:8000/docs

## 抽卡约定

1. `POST /api/v1/auth/login` 换 JWT。
2. `GET /api/v1/boxes` 取本期盲盒和奖池（对应盲盒页大奖网格）。
3. `POST /api/v1/boxes/{id}/draw` 传入 `target_prize_id`。选中的大奖权重提高 35%。
4. 未中大奖会命中「余额返还」，把本次 `price` 加回可提现余额。
5. 返还奖会附带一张招财卡，用于集卡进度。

## 主要接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/health` | 健康检查 |
| POST | `/api/v1/auth/sms` | 发送验证码（演示） |
| POST | `/api/v1/auth/login` | 登录 / 注册 |
| GET | `/api/v1/users/me` | 当前用户资产 |
| GET | `/api/v1/boxes` | 盲盒列表 |
| GET | `/api/v1/boxes/{id}` | 盲盒详情 |
| POST | `/api/v1/boxes/{id}/draw` | 抽一次 |
| GET | `/api/v1/draws/me` | 我的开盒记录 |
| GET | `/api/v1/cards/progress` | 集卡进度 |
| GET | `/api/v1/broadcast` | 首页中奖播报 |

请求示例：

```http
POST /api/v1/boxes/1/draw
Authorization: Bearer <token>
Content-Type: application/json

{"target_prize_id": 1}
```
