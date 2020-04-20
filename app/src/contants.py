import tensorflow as tf

# parameter for model

UNITS = 512

EMBEDDING_DIM = 300

DROPOUT_RATE = 0.3

BATCH_SIZE = 32

INP_VOCAB = 52081

TAR_VOCAB = 25499

MAX_LEN_INPUT = 69

MAX_LEN_TARGET = 86

OPTIMIZER = tf.keras.optimizers.Adam()
