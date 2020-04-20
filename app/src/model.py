import tensorflow as tf


class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_size, dropout_rate):
        super(Encoder, self).__init__()
        self.batch_size = batch_size
        self.enc_units = enc_units
        self.dropout = tf.keras.layers.Dropout(dropout_rate)
        self.embedding = tf.keras.layers.Embedding(
            vocab_size, embedding_dim)
        self.first_lstm = tf.keras.layers.LSTM(self.enc_units,
                                               return_sequences=True,
                                               recurrent_initializer='glorot_uniform')

        self.final_lstm = tf.keras.layers.LSTM(self.enc_units,
                                               return_sequences=True,
                                               return_state=True,
                                               recurrent_initializer='glorot_uniform')

    def call(self, x, hidden):
        x = self.embedding(x)
        x = self.dropout(x)
        x = self.first_lstm(x, initial_state=hidden)
        output, state_h, state_c = self.final_lstm(x)
        state = [state_h, state_c]

        return output, state

    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.enc_units)), tf.zeros((self.batch_size, self.enc_units))


class Attention(tf.keras.models.Model):

    def __init__(self, units: int, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.units = units

        self.q_dense_layer = tf.keras.layers.Dense(
            units, use_bias=False, name='q_dense_layer')
        self.k_dense_layer = tf.keras.layers.Dense(
            units, use_bias=False, name='k_dense_layer')
        self.v_dense_layer = tf.keras.layers.Dense(
            units, use_bias=False, name='v_dense_layer')
        self.output_dense_layer = tf.keras.layers.Dense(
            units, use_bias=False, name='output_dense_layer')

    def call(self, input, memory):

        q = self.q_dense_layer(input)
        k = self.k_dense_layer(memory)
        v = self.v_dense_layer(memory)

        depth = self.units // 2
        q *= depth ** -0.5  # for scaled dot production

        # caluclate relation between query and key
        logit = tf.matmul(q, k, transpose_b=True)

        attention_weight = tf.nn.softmax(logit)

        attention_output = tf.matmul(attention_weight, v)
        return self.output_dense_layer(attention_output)


class Decoder(tf.keras.Model):

    def __init__(self, vocab_size, embedding_dim, dec_units, batch_size, dropout_rate):
        super(Decoder, self).__init__()
        self.batch_size = batch_size
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(
            vocab_size, embedding_dim)
        self.dropout = tf.keras.layers.Dropout(dropout_rate)
        self.first_lstm = tf.keras.layers.LSTM(self.dec_units,
                                               return_sequences=True)
        self.final_lstm = tf.keras.layers.LSTM(self.dec_units,
                                               return_sequences=True,
                                               return_state=True)

        self.fc = tf.keras.layers.Dense(vocab_size)

        self.attention = Attention(self.dec_units)

    def call(self, x, hidden, enc_output):
        x = self.embedding(x)
        x = self.dropout(x)

        x = self.first_lstm(x)
        output, state_h, state_c = self.final_lstm(x)
        state = [state_h, state_c]
        attention_weights = self.attention(output, enc_output)
        output = tf.concat([output, attention_weights], axis=-1)

        output = tf.reshape(output, (-1, output.shape[2]))

        output = self.fc(output)

        return output, state
