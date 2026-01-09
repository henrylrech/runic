import handlers
import bot as bot_module

try:
    bot_module.run_bot()
except Exception as e:
    print(f"unexpected crash: {e}")