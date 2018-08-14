#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:35:29 2017

@author: huang
"""
# parameters for processing the dataset
DATA_PATH = './data/xiaohuangji'
LINE_FILE = 'xiaohuangji50w_nofenci.conv'
USER_DICT = './data_util/userdict.txt'
OUTPUT_FILE = 'output_convo.txt'
PROCESSED_PATH = './data/xiaohuangji/processed'
OVERALL_PROCESSED_PATH = './data/processed'
CPT_PATH = 'checkpoints'
CPT_PATH_FINAL = 'checkpoints_final'
SUMMARY_PATH = 'summaries'
BUCKETS=[(5,5),(5,10),(10,5),(10, 10), (15, 15), (20,20)]
num_buckets = 10

#######################
## data preprocess steps
start_point=0
training_size = None
testset_size = 0.001
max_conv_length = 6


#######################
## determine structure
#######################
bidirection = True
hrnn = False
## tensorboard
tensorboard = True
## load pretrained embeding
load_embeding = False

#######################
## number of gpus####
#######################
num_gpus = 1
colocate_gradients_with_ops = False

    
#######################
## model_inputs 
#######################
cell_type = 'layer_norm_lstm' ## lstm gru nas

epochs = 40
batch_size = 32
rnn_size = 1024
attention_size = 1024

# Number of Layers
num_layers = 2 #this is the number of bi directional layers, was messy to change variable names
assert num_layers % 2 == 0
num_layers = int(num_layers/2)
num_uni_layers = 4 #this is the number of uni directional layers
decoder_num_layers = 6
num_residual_layers = 0 
assert num_layers*2 + num_uni_layers == decoder_num_layers

# Embedding Size
encoding_embedding_size = 300
decoding_embedding_size = 300
keep_probability = 0.8
max_target_sentence_length= 31

src_max_len = 30
tgt_max_len = 30

beam_width = 3
source_vocab_size = 100000
target_vocab_size = 100000
max_gradient_norm = 5.0

# exponential learning rate decaly prams 
# Learning Rate
learning_rate = 1e-3
learning_rate_decay_scheme = False
clear_step = False
start_decay_step = 50000
decay_steps = 200000
decay_factor = 0.5

###################
### display steps##
###################
display_step = 200
save_step = 2000
start_shufle = 1











