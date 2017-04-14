# -*- coding: utf-8 -*-

from vmts_jsonrpc_protocol import WebsocketJsonRpcProtocol,gen_id,WebsocketJsonRpcProtocolConstructor
import re, json
import pytest


test_string = ["\n", "1+1", "1==1", "True", "False", "!@#$%^&*", "\\", "None", "", "."]
test_string_1 = ["", "111", "qweqr", "12WfWwffrhbtkljhnjksfwfwfwfwwfvhbej", "None", "True", "False", "."]


class TestGenid:

    @staticmethod
    def gen_id_test(func, dev_id=None):
        """
        Test func:gen_id.
        :param func: function object which is tested.
        :param dev_id: parameter of func tested(could be None).
        :return: <bool> return of function matching or not.
        """
        res = func(dev_id)
        obj = re.match("%s-\d+" % dev_id if dev_id is not None else "root_server_#0", res)
        if obj:
            return True
        else:
            return False

    def test_gen_id(self):
        """
        Test func:gen_id.
        """
        for i in test_string_1:
            assert self.gen_id_test(gen_id, i) == True


class TestWJRP:

    def test_argtype(self):
        """
        Test class func:WebsocketJsonRpcProtocol.__init__.
        """
        with pytest.raises(Exception):
            wjrp_arg_type = WebsocketJsonRpcProtocol()

    def test_ver(self):
        """
        Test class func:WebsocketJsonRpcProtocol._ver().
        """
        assert WebsocketJsonRpcProtocol._ver() == '1.0.0'

    @staticmethod
    def request_test(inst):
        """
        Test class:WebsocketJsonRpcProtocol Instance:request.
        :param inst: <object> Instance:request.
        """
        assert re.match("root_server_#0-\d+", inst.uid)
        for i in test_string:
            res = inst.pack(i, name=i)
            obj = json.loads(res)
            assert obj['method'] == [i]
            assert obj['params'] == {"name": i}
            res_uid, res_method, res_params = inst.unpack(res)
            assert re.match("root_server_#0-\d+", res_uid)
            assert res_method == [i]
            assert res_params == {"name": i}

    def test_request(self):
        """
        Test class:WebsocketJsonRpcProtocol Instance:request.
        """
        wjrp_request = WebsocketJsonRpcProtocol("request")
        self.request_test(wjrp_request)

    @staticmethod
    def response_test(inst):
        """
        Test class:WebsocketJsonRpcProtocol Instance:response.
        :param inst: <object> Instance:response.
        """
        for i in test_string:
            res = inst.pack(uid=i, result=i, err=i)
            obj = json.loads(res)
            assert obj['id'] == i
            assert obj['result'] == i
            assert obj['error'] == i
            res_uid, res_result, res_err = inst.unpack(res)
            assert res_uid == i
            assert res_result == i
            assert res_err == i

    def test_response(self):
        """
        Test class:WebsocketJsonRpcProtocol Instance:response.
        """
        wjrp_response = WebsocketJsonRpcProtocol("response")
        self.response_test(wjrp_response)


class TestWJRPC:

    def test_wjrpc(self):
        """
        Test class:WebsocketJsonRpcProtocolConstructor.
        """
        wjrpcj_response = WebsocketJsonRpcProtocolConstructor("response")
        assert wjrpcj_response.version == '1.0.0'
        TestWJRP.response_test(wjrpcj_response.instance)
        TestWJRP.response_test(wjrpcj_response.__enter__())
        wjrpcj_response.__exit__(exc_type=None, exc_val=1, exc_tb=1)
        with pytest.raises(AttributeError):
            wjrpcj_response.instance
        wjrpcj_request = WebsocketJsonRpcProtocolConstructor("request")
        assert wjrpcj_request.version == '1.0.0'
        TestWJRP.request_test(wjrpcj_request.instance)
        TestWJRP.request_test(wjrpcj_request.__enter__())
        wjrpcj_request.__exit__(exc_type=None, exc_val=1, exc_tb=1)
        with pytest.raises(AttributeError):
            wjrpcj_request.instance

