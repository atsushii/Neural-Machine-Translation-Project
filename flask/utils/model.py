import tensorflow as tf
import config as cfg
import numpy as np
import pdb


def create_model(model):

    # encoder model
    encoder_input = model.input[0]  # encoder input
    encoder_output, state_h, state_c = model.layers[6].output  # encoder lstm
    encoder_state = [state_h, state_c]
    encoder_m = tf.keras.models.Model(encoder_input, encoder_state)

    # decoder model
    decoder_input = model.input[1]  # decoder input
    decoder_state_input_h = tf.keras.layers.Input(shape=(cfg.UNITS,))
    decoder_state_input_c = tf.keras.layers.Input(shape=(cfg.UNITS,))
    decoder_state_input = [decoder_state_input_h, decoder_state_input_c]
    decoder_emb_layer = model.layers[3]
    decoder_emb = decoder_emb_layer(decoder_input)
    decoder_lstm = model.layers[7]  # decoder lstm
    decoder_output, dec_state_h, dec_state_c = decoder_lstm(decoder_emb, initial_state=decoder_state_input)
    decoder_state = [dec_state_h, dec_state_c]

    decoder_dense = model.layers[16]
    decoder_outputs = decoder_dense(decoder_output)

    decoder_m = tf.keras.models.Model([decoder_input] + decoder_state_input, [decoder_outputs] + decoder_state)

    return encoder_m, decoder_m


def decoder_seq(encoder, decoder, input_seq, japanese_tokens):
    pdb.set_trace()
    # encoder the input seq as vector
    state_en = encoder.predict(input_seq)
    # generate empty target sequence
    target_seq = np.zeros((1, cfg.MAX_OUTPUT_SIZE))
    # populate the first character of target seq
    target_seq[0, 0] = 1

    # loop for batch of sequences
    stop_condition = False
    decoder_sentence = ' '

    while not stop_condition:
        output_token, h, c = decoder.predict([target_seq] + state_en)

        sampled_token_index = np.argmax(output_token[0, -1, :])
        sampled_char = japanese_tokens[sampled_token_index]
        decoder_sentence += ' ' + sampled_char

        # stop condition
        if sampled_char == "_END" or len(decoder_sentence) > cfg.MAX_INPUT_SIZE:
            stop_condition = True

        # update the target sequence
        predict_result = np.zeros((1, cfg.MAX_OUTPUT_SIZE))
        predict_result[0, 0] = 1.

        # update states
        state_en = [h, c]

    return predict_result[: -4]
