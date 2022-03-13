import pytest
import requests
import random
@pytest.fixture()
def gettoken():
    # 作用1：返回值
    return "9232aaa55e0a419e9a863c91007f7bf1"


def test_insert_produst(gettoken):
    num=int(random.randint(0,1000))
    url='http://192.168.37.130:9091/v1/products'
    json={"product_name":"浩云彩灯","product_key":"HY-COLOR-LIGHT"+str(num),
    "class_id":"123456","is_standard":True,"pid":"","product_node_type":0,
    "dynamic_register_enable":0,
    "tags":{
        "manufacturers":"浩云"
    }
}
    headers={"Content-Type":"application/json","Authorization":gettoken}
    request=requests.post(url=url,
                  json=json,
                  headers=headers
                  )
    assert request.json()['product_key']==json['product_key']


if __name__ == '__main__':
    pytest.mian("-s","-v","./test_fixtrue.py")