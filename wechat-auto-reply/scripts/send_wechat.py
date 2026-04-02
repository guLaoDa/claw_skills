#!/usr/bin/env python3
"""
微信自动发送消息脚本

通过模拟键盘输入，在微信电脑客户端自动发送消息。

使用方式:
    python send_wechat.py --contact "联系人姓名" --message "消息内容"

依赖:
    pip install pyautogui pyperclip pygetwindow
"""

import sys
import argparse
import time

try:
    import pyautogui
    import pyperclip
    import pygetwindow
except ImportError as e:
    print(f"Error: Missing dependency - {e}")
    print("Please install: pip install pyautogui pyperclip pygetwindow")
    sys.exit(1)


# 配置
WECHAT_WINDOW_TITLE = "微信"
SEARCH_DELAY = 0.5  # 搜索后等待时间
MESSAGE_DELAY = 0.3  # 输入消息后等待时间


def find_wechat_window():
    """查找微信窗口"""
    windows = pygetwindow.getWindowsWithTitle(WECHAT_WINDOW_TITLE)
    if not windows:
        # 尝试其他可能的窗口标题
        windows = pygetwindow.getWindowsWithTitle("WeChat")
    if not windows:
        return None
    return windows[0]


def activate_wechat(window):
    """激活微信窗口"""
    try:
        window.activate()
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f"Failed to activate window: {e}")
        return False


def search_contact(contact_name):
    """
    搜索联系人
    
    流程: Ctrl+F -> 输入联系人名 -> Enter
    """
    # 使用 Ctrl+F 打开搜索
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(SEARCH_DELAY)
    
    # 清空搜索框并输入联系人名称
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    
    # 复制联系人名称到剪贴板（处理中文）
    pyperclip.copy(contact_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(SEARCH_DELAY)
    
    # 按 Enter 打开聊天窗口
    pyautogui.press('enter')
    time.sleep(0.5)


def send_message(message):
    """
    发送消息
    
    流程: 粘贴消息 -> Enter 发送
    """
    # 复制消息内容到剪贴板（处理中文）
    pyperclip.copy(message)
    
    # 粘贴消息
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(MESSAGE_DELAY)
    
    # 按 Enter 发送
    pyautogui.press('enter')


def main():
    parser = argparse.ArgumentParser(description='微信自动发送消息')
    parser.add_argument('--contact', required=True, help='联系人姓名')
    parser.add_argument('--message', required=True, help='要发送的消息内容')
    
    args = parser.parse_args()
    
    print(f"开始发送消息...")
    print(f"联系人: {args.contact}")
    print(f"消息内容: {args.message}")
    
    # 1. 查找微信窗口
    print("\n[1/4] 查找微信窗口...")
    window = find_wechat_window()
    if not window:
        print("Error: 未找到微信窗口，请确保微信已打开")
        sys.exit(1)
    print(f"找到窗口: {window.title}")
    
    # 2. 激活微信窗口
    print("\n[2/4] 激活微信窗口...")
    if not activate_wechat(window):
        print("Error: 无法激活微信窗口")
        sys.exit(1)
    print("窗口已激活")
    
    # 3. 搜索联系人
    print("\n[3/4] 搜索联系人...")
    search_contact(args.contact)
    print(f"已打开与 {args.contact} 的聊天窗口")
    
    # 4. 发送消息
    print("\n[4/4] 发送消息...")
    send_message(args.message)
    print("消息已发送!")
    
    print("\n完成!")


if __name__ == "__main__":
    # pyautogui 安全设置
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    
    main()
