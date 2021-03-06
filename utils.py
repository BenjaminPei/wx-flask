import hashlib

token = "clown1988"


def check_token(request):
    # 1、 获取携带的 signature、timestamp、nonce、echostr
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    echostr = request.args.get("echostr", "")
    print(signature, timestamp, nonce, echostr)

    # 2、 进行字典排序
    data = [token, timestamp, nonce]
    data.sort()

    # 3、三个参数拼接成一个字符串并进行sha1加密
    temp = ''.join(data)
    sha1 = hashlib.sha1(temp.encode('utf-8'))
    hashcode = sha1.hexdigest()
    print(hashcode)

    # 4、对比获取到的signature与根据上面token生成的hashcode，如果一致，则返回echostr，对接成功
    if hashcode == signature:
        return echostr
    else:
        return "error"
