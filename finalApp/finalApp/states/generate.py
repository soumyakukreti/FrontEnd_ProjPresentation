import tensorflow as tf
import glob
# import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras import layers

BATCH_SIZE = 256
NOISE_DIM = 50

IMG_SIZE = 64





# Generator Model

FILTER_COUNT = 16
IN_LAYER_COUNT = 6


def make_generator_model():
    model = tf.keras.Sequential()
    model.add(layers.Dense(
        (IMG_SIZE//(2**IN_LAYER_COUNT))*(IMG_SIZE//(2**IN_LAYER_COUNT))*NOISE_DIM, use_bias=False, input_shape=(NOISE_DIM,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Reshape((IMG_SIZE//(2**IN_LAYER_COUNT),
              IMG_SIZE//(2**IN_LAYER_COUNT), NOISE_DIM)))

    for i in range(IN_LAYER_COUNT):
        model.add(layers.Conv2DTranspose(FILTER_COUNT*2**(IN_LAYER_COUNT-i-1),
                  (6, 6), strides=(2, 2), padding='same', use_bias=False))
        model.add(layers.BatchNormalization())
        model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(3, (6, 6), strides=(1, 1),
                                     padding='same', use_bias=False, activation='sigmoid'))
    assert model.output_shape == (None, IMG_SIZE, IMG_SIZE, 3)

    return model



generator = make_generator_model()

noise = tf.random.normal([1, NOISE_DIM])
generated_image = generator(noise, training=False)



# Discriminator Model

DISC_FILTER_COUNT = FILTER_COUNT
def make_discriminator_model():
    model = tf.keras.Sequential()
    model.add(layers.Conv2D(DISC_FILTER_COUNT, (6, 6), strides=(2, 2), padding='same',
                                     input_shape=[IMG_SIZE, IMG_SIZE, 3]))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    for i in range(1, IN_LAYER_COUNT):
        model.add(layers.Conv2D(DISC_FILTER_COUNT*(2**i), (6, 6), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU())
        model.add(layers.Dropout(0.3))

    model.add(layers.Flatten())
    model.add(layers.Dense(1,activation='sigmoid'))

    return model



discriminator = make_discriminator_model()
decision = discriminator(generated_image)


cross_entropy = tf.keras.losses.BinaryCrossentropy()

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)

generator_optimizer = tf.keras.optimizers.legacy.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.legacy.Adam(1e-4)

checkpoint_dir = '/Users/siddharth/desktop/NTCCPyproj/cats-gan/models'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                                 discriminator_optimizer=discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)


num_examples_to_generate = 16

seed = tf.random.normal([num_examples_to_generate, NOISE_DIM])


def print():

    checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir)).expect_partial()

    noise = tf.random.normal([1, NOISE_DIM])
    generated_image = generator(noise, training=False)
    decision = discriminator(generated_image, training=False)
    plt.savefig('/Users/siddharth/desktop/NTCCPyproj/cats-gan/generated')

