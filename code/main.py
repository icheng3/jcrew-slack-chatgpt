import os
import argparse
import numpy as np
import pickle
import tensorflow as tf
from typing import Optional
from types import SimpleNamespace

from scraper import indexer as idxr
from scraper import scraper as scr

CURR_SITEMAP = 'https://jcrew.com'

def parse_args(args=None):
    """ 
    Perform command-line argument parsing (other otherwise parse arguments with defaults). 
    To parse in an interative context (i.e. in notebook), add required arguments.
    These will go into args and will generate a list that can be passed in.
    For example: 
        parse_args('--type', 'rnn', ...)
    """
    parser = argparse.ArgumentParser(description="Let's train some neural nets!", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--type',           required=True,              choices=['rnn', 'transformer'],     help='Type of model to train')
    parser.add_argument('--task',           required=True,              choices=['train', 'test', 'both'],  help='Task to run')
    parser.add_argument('--data',           required=True,              help='File path to the assignment data file.')
    parser.add_argument('--epochs',         type=int,   default=3,      help='Number of epochs used in training.')
    parser.add_argument('--lr',             type=float, default=1e-3,   help='Model\'s learning rate')
    parser.add_argument('--optimizer',      type=str,   default='adam', choices=['adam', 'rmsprop', 'sgd'], help='Model\'s optimizer')
    parser.add_argument('--batch_size',     type=int,   default=100,    help='Model\'s batch size.')
    parser.add_argument('--hidden_size',    type=int,   default=256,    help='Hidden size used to instantiate the model.')
    parser.add_argument('--window_size',    type=int,   default=20,     help='Window size of text entries.')
    parser.add_argument('--chkpt_path',     default='',                 help='where the model checkpoint is')
    parser.add_argument('--check_valid',    default=True,               action="store_true",  help='if training, also print validation after each epoch')
    if args is None: 
        return parser.parse_args()      ## For calling through command line
    return parser.parse_args(args)      ## For calling through notebook.


def main(args):
    jcrew_scraper = scr.Scraper(url=CURR_SITEMAP)
    jcrew_scraper.pdp = [f'https://www.jcrew.com/sitemap-wex/sitemap-pdp{i}.xml' for i in range(1, 5)]







    # ##############################################################################
    # ## Data Loading
    # with open(args.data, 'rb') as data_file:
    #     data_dict = pickle.load(data_file)

    # feat_prep = lambda x: np.repeat(np.array(x).reshape(-1, 2048), 5, axis=0)
    # # img_prep  = lambda x: np.repeat(x, 5, axis=0)
    # train_captions  = np.array(data_dict['train_captions'])
    # test_captions   = np.array(data_dict['test_captions'])
    # train_img_feats = feat_prep(data_dict['train_image_features'])
    # test_img_feats  = feat_prep(data_dict['test_image_features'])
    # # train_images    = img_prep(data_dict['train_images'])
    # # test_images     = img_prep(data_dict['test_images'])
    # word2idx        = data_dict['word2idx']
    # # idx2word        = data_dict['idx2word']

    # ##############################################################################
    # ## Training Task
    # if args.task in ('train', 'both'):
        
    #     ##############################################################################
    #     ## Model Construction
    #     decoder_class = {
    #         'rnn'           : RNNDecoder,
    #         'transformer'   : TransformerDecoder
    #     }[args.type]

    #     decoder = decoder_class(
    #         vocab_size  = len(word2idx), 
    #         hidden_size = args.hidden_size, 
    #         window_size = args.window_size
    #     )
        
    #     model = ImageCaptionModel(decoder)
        
    #     compile_model(model, args)
    #     train_model(
    #         model, train_captions, train_img_feats, word2idx['<pad>'], args, 
    #         valid = (test_captions, test_img_feats)
    #     )
    #     if args.chkpt_path: 
    #         ## Save model to run testing task afterwards
    #         save_model(model, args)
                
    # ##############################################################################
    # ## Testing Task
    # if args.task in ('test', 'both'):
    #     if args.task != 'both': 
    #         ## Load model for testing. Note that architecture needs to be consistent
    #         model = load_model(args)
    #     if not (args.task == 'both' and args.check_valid):
    #         test_model(model, test_captions, test_img_feats, word2idx['<pad>'], args)

    # ##############################################################################

##############################################################################
## UTILITY METHODS



## END UTILITY METHODS
##############################################################################

if __name__ == '__main__':
    main(parse_args())
