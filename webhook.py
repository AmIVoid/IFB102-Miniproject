from dhooks import Webhook

hook = Webhook('https://discord.com/api/webhooks/844032616532934667/Oju-XiN5e3eFPwxlosFopHgtlJitmWC0JuIEoR1I8NrKNk48vFfQz8atL4zThR1rqKX6')

def sendMessage(message):
    hook.send(message)