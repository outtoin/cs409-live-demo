from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
import pickle
import json
import tempfile

from collections import defaultdict

from keras.models import model_from_json, load_model
from keras.preprocessing.sequence import pad_sequences

from app.config import *

os.environ['KMP_DUPLICATE_LIB_OK']='True'

import matplotlib.font_manager as fm
path = '/usr/share/fonts/NanumBarunGothicLight.ttf'
font_name = fm.FontProperties(fname=path, size=50).get_name()
print(font_name)
plt.rc('font', family=font_name)

def get_activations(model, inputs, print_shape_only=False, layer_name=None):
    # Documentation is available online on Github at the address below.
    # From: https://github.com/philipperemy/keras-visualize-activations
#     print('----- activations -----')
    activations = []
    inp = model.input
    if layer_name is None:
        outputs = [layer.output for layer in model.layers]
    else:
        outputs = [layer.output for layer in model.layers if layer.name == layer_name]  # all layer outputs
    funcs = [K.function([inp] + [K.learning_phase()], [out]) for out in outputs]  # evaluation functions
    layer_outputs = [func([inputs, 1.])[0] for func in funcs]
    for layer_activations in layer_outputs:
        activations.append(layer_activations)
    return activations


class MlUtils(object):
    def __init__(self):
        self._model_file = os.path.join(ASSETS_DIR, 'model.json')
        self._weight_file = os.path.join(ASSETS_DIR, 'model.h5')
        self._tokenizer_file = os.path.join(ASSETS_DIR, 'tokenizer.pickle')
        self._data_prob_file = os.path.join(ASSETS_DIR, 'data_prob.json')
        
        
        print("Load Assets...")
        self._load()
        print("Successfully Loaded Assets!")

    def _load(self):
        # load keras model
        with open(self._model_file, 'r') as f:
            json_file = f.read()
        self.model = model_from_json(json_file)
        self.model.load_weights(self._weight_file)
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # load tokenizer  
        with open(self._tokenizer_file, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
            
        token_index = self.tokenizer.word_index
        self.token_index_inv = {v: k for k, v in token_index.items()}

        # load data_prob
        with open(self._data_prob_file, 'r') as prob:
            self.data_prob = json.loads(prob.read())

    def _make_preprocessed_text(self, text):
        tokenized_text = self.tokenizer.texts_to_sequences([text])
        pad_seq = pad_sequences(tokenized_text, maxlen=MAXLEN)
        return tokenized_text, pad_seq
    
    def _predict(self, prep_t):
        return not not round(self.model.predict(prep_t)[0][0])
    
    def _make_attention_fig(self, tkn_t, prep_t):
        inputs = np.array(prep_t)
        attention_vector = np.mean(get_activations(self.model,
                                               inputs,
                                               print_shape_only=True,
                                               layer_name='attention_vec')[0], axis=2).squeeze()
        
        token_values_after_lookup = [self.token_index_inv.get(item, item) for item in tkn_t[0]]
        data = np.array(attention_vector[-(len(token_values_after_lookup)):])
        data = data / np.sum(data)
    
        result_dict = defaultdict(int)
        for a, t in zip(data, token_values_after_lookup):
            result_dict[t] += a
        res = sorted(result_dict.items(), key=lambda kv: kv[1], reverse=True)
        
        # make fig
        f, ax = plt.subplots(figsize=(30, 12))
        pd.DataFrame(data, columns=['attention (%)']).plot(kind='bar',
                                                   title='XAI Value of input texts.',
                                                   ax=ax)
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(18)
        ax.xaxis.set_ticklabels(token_values_after_lookup)
        
        # make tempdir
        # tmp = tempfile.mkdtemp()
        path = os.path.join('app', 'static', 'img', 'fig1.png')
        f.savefig(path)
        
        return res[0], path 
    
    def make_predict(self, text):
        tokenized_text, preprocessed_text = self._make_preprocessed_text(text)
        pred = self._predict(preprocessed_text)
        fig = self._make_attention_fig(tokenized_text, preprocessed_text)
        
        return pred, fig
        
    def make_top_list(self, n=10):
        res = [(k, self.data_prob[k]) for k in sorted(self.data_prob, key=self.data_prob.get, reverse=True)]
#         res = sorted(self.data_prob.items(), reverse=True)
        data = {k: v for k, v in res[:n]}
        xt = [k for k, v in res[:n]]
        yt = [v for k, v in res[:n]]
        f, ax = plt.subplots(figsize=(20, 12))
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(15)
        ax.bar([i for i in range(len(data))], list(yt))
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start+1, end, 1.0))
        ax.xaxis.set_ticklabels(xt)
        
        # tmp = tempfile.mkdtemp()
        path = os.path.join('app', 'static', 'img', 'fig2.png')
        f.savefig(path)
        
        return data, path

if __name__ == "__main__":
    from PIL import Image

    mlu = MlUtils()
    data, path = mlu.make_top_list()
    pred, fig = mlu.make_predict('안녕하세요! 안녕하세요! 안녕하세요!')

    im = Image.open(path)
    im.show()

    im = Image.open(fig[1])
    im.show()
