# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W7x-8mBq_uZ56BoVaHJBRHA-Z8msYOp5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch import optim
from torch.nn import functional as F 
from torch.optim.lr_scheduler import _LRScheduler

from recochef.datasets.movielens import MovieLens
from recochef.preprocessing.encode import label_encode
from recochef.utils.iterators import batch_generator
from recochef.models.embedding import EmbeddingNet

import math
import copy
import pickle
import numpy as np
import pandas as pd
from textwrap import wrap
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
plt.style.use('ggplot')
from tqdm import tqdm
import time
class MLP(nn.Module):
    def __init__(self, embedding_size, hidden_size,num_users,num_items):
        super(MLP, self).__init__()
        self.user_embeddings = nn.Embedding(num_users, embedding_size)
        self.item_embeddings = nn.Embedding(num_items, embedding_size)
        self.Rec = nn.Sequential(
                      nn.Linear(embedding_size*2, hidden_size),
                      nn.ReLU(inplace=True),
                      nn.Linear(hidden_size, 1))

    def forward(self,user_id,item_id):
        self.user_embedding = self.user_embeddings(user_id)
        self.item_embedding = self.item_embeddings(item_id)
        x = torch.cat([self.user_embedding, self.item_embedding], dim=1)
        x = self.Rec(x)
        return x