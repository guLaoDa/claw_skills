---
name: wechat-auto-reply
description: 微信自动回复技能。通过模拟键盘输入，在微信电脑客户端自动发送消息。触发关键词：微信回复、发微信、回微信、wechat、微信自动回复。当用户要求给某人发微信、回复微信消息时使用此技能。
---

# 微信自动回复

通过模拟键盘输入，在微信电脑客户端自动发送消息。

## 功能

- 激活微信窗口
- 搜索联系人
- 输入消息并发送

## 使用方式

```bash
conda activate base
python scripts/send_wechat.py --contact "联系人姓名" --message "消息内容"
```

## 参数说明

| 参数 | 说明 | 必填 |
|------|------|------|
| `--contact` | 联系人姓名（微信中显示的名称） | 是 |
| `--message` | 要发送的消息内容 | 是 |

## 注意事项

1. **微信窗口必须已登录** - 脚本不会自动登录微信
2. **发送时窗口会跳到前台** - 这是模拟键盘输入的限制
3. **发送速度** - 脚本会有短暂延迟确保操作稳定
4. **联系人名称** - 必须与微信中显示的名称完全一致

## 依赖

- pyautogui
- pyperclip
- pygetwindow

安装依赖：
```bash
conda activate base
pip install pyautogui pyperclip pygetwindow
```

## 工作流程

1. 检查微信窗口是否存在
2. 激活微信窗口
3. 使用 Ctrl+F 打开搜索
4. 输入联系人名称
5. 按 Enter 打开聊天窗口
6. 输入消息内容
7. 按 Enter 发送
