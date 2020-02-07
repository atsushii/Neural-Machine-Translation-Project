import tensorflow as tf
import config as cfg
import numpy as np
import pdb


class CreateModel(object):

    def __init__(self, model):

        super(CreateModel, self).__init__()

        self.model = model

    def __call__(self):

        # encoder model
        encoder_input = self.model.input[0]  # encoder input
        encoder_output, state_h, state_c = self.model.layers[6].output  # encoder lstm
        encoder_state = [state_h, state_c]
        encoder_m = tf.keras.models.Model(encoder_input, encoder_state)
        # encoder_m._make_predict_function()

        # decoder model
        decoder_input = self.model.input[1]  # decoder input
        decoder_state_input_h = tf.keras.layers.Input(shape=(cfg.UNITS,))
        decoder_state_input_c = tf.keras.layers.Input(shape=(cfg.UNITS,))
        decoder_state_input = [decoder_state_input_h, decoder_state_input_c]
        decoder_emb_layer = self.model.layers[3]
        decoder_emb = decoder_emb_layer(decoder_input)
        decoder_lstm = self.model.layers[7]  # decoder lstm
        decoder_output, dec_state_h, dec_state_c = decoder_lstm(decoder_emb, initial_state=decoder_state_input)
        decoder_state = [dec_state_h, dec_state_c]

        decoder_dense = self.model.layers[16]
        decoder_outputs = decoder_dense(decoder_output)

        decoder_m = tf.keras.models.Model([decoder_input] + decoder_state_input, [decoder_outputs] + decoder_state)
        # decoder_m._make_predict_function()
        return encoder_m, decoder_m


class Predict(object):

    def __init__(self, encoder, decoder, japanese_tokens):

        super(Predict, self).__init__()
        self.graph = tf.get_default_graph()
        self.encoder = encoder
        self.encoder._make_predict_function()
        self.decoder = decoder
        self.decoder._make_predict_function()
        self.session = tf.keras.backend.get_session()
        self.japanese_tokens = japanese_tokens
        self.graph = tf.get_default_graph()

    def result(self, input_seq):

        with self.session.as_default():
            # encoder the input seq as vector
            with self.graph.as_default():
                state_en = self.encoder.predict(input_seq)
        # generate empty target sequence
        target_seq = np.zeros((1, cfg.MAX_OUTPUT_SIZE))
        # populate the first character of target seq
        target_seq[0, 0] = 1

        # loop for batch of sequences
        stop_condition = False
        decoder_sentence = ' '

        while not stop_condition:
            with self.session.as_default():
                with self.graph.as_default():
                    output_token, h, c = self.decoder.predict([target_seq] + state_en)
            sampled_token_index = np.argmax(output_token[0, -1, :])
            sampled_char = self.japanese_tokens[str(sampled_token_index)]
            decoder_sentence += ' ' + sampled_char

            # stop condition
            if sampled_char == "_END" or len(decoder_sentence) > cfg.MAX_INPUT_SIZE:
                stop_condition = True

            # update the target sequence
            target_seq = np.zeros((1, cfg.MAX_OUTPUT_SIZE))
            target_seq[0, 0] = 1.

            # update states
            state_en = [h, c]
        return decoder_sentence[: -4]
