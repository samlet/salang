import json

class IndonesiaNer(object):
    """
    >>> from sal.id.indonesia_ner import IndonesiaNer
    """
    def __init__(self):
        from py4j.java_gateway import JavaGateway, JavaObject, GatewayParameters
        # from py4j.java_gateway import java_import, get_field
        # from sagas.conf.runtime import runtime
        # host = "localhost" if not runtime.is_docker() else 'ruleprocs'
        host="localhost"
        port = 4333
        callback_port = 4334
        self.gateway = JavaGateway(python_proxy_port=callback_port,
                              gateway_parameters=GatewayParameters(address=host, port=port, auto_field=True))
        self.j = self.gateway.new_jvm_view()

    def id_parse(self, sents):
        ner = self.gateway.entry_point.getIndonesiaNer()
        return json.loads(ner.nerJson(sents))

    def ner(self, sents):
        running_offset = 0
        rs = []
        tokens = self.id_parse(sents)
        for token in tokens:
            word = token['token']
            word_offset = sents.index(word, running_offset)
            word_len = len(word)
            running_offset = word_offset + word_len
            rs.append({"start": word_offset,
                       "end": running_offset,
                       'text': word, 'entity': token['xmlTag']
                       })
        return [w for w in rs if w['entity'] != 'OTHER']

id_ner=IndonesiaNer()


