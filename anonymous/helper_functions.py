import shortuuid
import json
from .models import Anonymous, Messages

def generate_code_user(request):
    id = shortuuid.ShortUUID().random(length=6)
    try:
        user_acc = Anonymous.objects.filter(user = request.user)
    except:
        user_acc = Anonymous.objects.create(user = request.user, code = id)
        return user_acc.code
    if user_acc:
        if user_acc[0].code:
            pass
        else:
             user_acc = Anonymous.objects.filter(user = request.user).create(code = id)
    else:
        user_acc = Anonymous.objects.create(user = request.user, code = id)
        return user_acc.code
    return user_acc[0].code

def get_messages(room_name):
    get_messages = Messages.objects.filter(room_name = room_name).order_by('date_time')
    pass_json = {'message':[]}

    for message in get_messages:
        pass_json['message'].append(message.message)
        
    messages = json.dumps(pass_json)
    return messages