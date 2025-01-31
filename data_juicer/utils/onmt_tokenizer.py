import pickle
import pyonmttok

class PickleableTokenizer(pyonmttok.Tokenizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._saved_params = {**kwargs}

    def __getstate__(self):
        return self._saved_params 

    def __setstate__(self, state):
        self.__init__(**state)

if __name__ == "__main__":

    # 创建一个 tokenizer
    tokenizer = PickleableTokenizer(mode="conservative")
    print(tokenizer("This is a test."))

    # 尝试 pickle
    pickled_tokenizer = pickle.dumps(tokenizer)

    # 反序列化
    unpickled_tokenizer = pickle.loads(pickled_tokenizer)

    # print(unpickled_tokenizer)  # 现在它可以被正常反序列化
    print(unpickled_tokenizer("This is a test."))
