print("Hello World")
"import termux
import textwrap

# retrieve various device infos
print(termux.wifi_connectioninfo())
print(termux.camera_info())
print(termux.telephony_deviceinfo())

# pretty print last 100 sms
messages = termux.sms_list(limit=100)

for m in messages:
    if 'sender' in m:
        print(f"{m['sender']}:")
    else:
        print(f"{m['number']}:")
    wrap = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
    body = wrap.fill(m["body"])
    print(body)

# send a message
termux.sms_send("sending an sms from python", "+01020304050")

# perform an action if the fingerprint matches
ret = termux.fingerprint(title="Restricted action", desc="Analyze your fingerprint")
if ret['auth_result'] == 'AUTH_RESULT_SUCCESS':
    print("Access granted")
else:
    print("Access denied")

# text to speech
termux.tts_speak("job's done !")"
 https://github.com/setiawanjemy88/termux_python#:~:text=import%20termux%0Aimport,job%27s%20done%20!%22)
