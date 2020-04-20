from .preprocessing import Preprocess
import tensorflow as tf


class Predict():

    def __init__(self, encoder, decoder, units, max_len_input, max_len_target, input_token, target_token, input_text):

        self.encoder = encoder
        self.decoder = decoder
        self.units = units
        self.max_len_input = max_len_input
        self.max_len_target = max_len_target
        self.input_token = input_token
        self.target_token = target_token
        self.input_text = input_text
        self.preprocess = Preprocess(input_text)

    def predict(self):

        sentence = self.preprocess.normalize()
        inputs = [self.input_token.word_index[i] for i in sentence.split()]

        inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs],
                                                               maxlen=self.max_len_input,
                                                               padding='post')

        inputs = tf.convert_to_tensor(inputs)
        result = ''
        hidden = [tf.zeros((1, self.units)), tf.zeros((1, self.units))]
        enc_out, state = self.encoder(inputs, hidden)
        hidden_state = state
        dec_input = tf.expand_dims([self.target_token.word_index['start_']], 0)
        for i in range(self.max_len_target):
            predictions, hidden_state = self.decoder(dec_input,
                                                     hidden_state,
                                                     enc_out)
            predicted_id = tf.argmax(predictions[0]).numpy()

            result += self.target_token.index_word[predicted_id]
            if self.target_token.index_word[predicted_id] == '_end' or len(result) > self.max_len_target:
                return result, self.input_text

            # the predicted ID is fed back into the model
            dec_input = tf.expand_dims([predicted_id], 0)
        return result, self.input_text
