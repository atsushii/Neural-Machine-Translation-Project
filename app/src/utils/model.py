import tensorflow as tf
from ..model import Encoder, Decoder
import pickle


class Model():

    def __init__(self, inp_vocab, tar_vocab, embedding_dim, units, batch_size, dropout_rate, optimizer):
        self.inp_vocab = inp_vocab
        self.tar_vocab = tar_vocab
        self.embedding_dim = embedding_dim
        self.units = units
        self.batch_size = batch_size
        self.dropout_rate = dropout_rate
        self.optimizer = optimizer

    def define_model(self):

        # initialize model
        encoder = Encoder(vocab_size=self.inp_vocab, embedding_dim=self.embedding_dim,
                          enc_units=self.units, batch_size=self.batch_size, dropout_rate=self.dropout_rate)

        decoder = Decoder(vocab_size=self.tar_vocab, embedding_dim=self.embedding_dim,
                          dec_units=self.units, batch_size=self.batch_size, dropout_rate=self.dropout_rate)

        model = tf.train.Checkpoint(optimizer=self.optimizer,
                                    encoder=encoder,
                                    decoder=decoder)
        # load trained model
        model.restore("src/static/model/ckpt-5")

        encoder = model.encoder
        decoder = model.decoder

        # load word tokens
        with open("src/static/word_token/input_lang_tokenize.pickle", "rb") as f:
            input_token = pickle.load(f)

        with open("src/static/word_token/target_lang_tokenize.pickle", "rb") as f:
            target_token = pickle.load(f)

        return encoder, decoder, input_token, target_token
