class hparams:
    # audio parameters
    num_mels = 80
    fmin = 125
    fmax = 7600
    fft_size = 1024
    hop_size = 256
    sample_rate = 22050
    preemphasis = 0.97
    min_level_db = -100
    ref_level_db = 20
    rescaling = False
    rescaling_max = 0.999
    allow_clipping_in_normalization = True

    max_iters=200
    griffin_lim_iters=60
    power=1.5        

    # preprocessing parameters
    min_text = 20

    # general parameters
    language = "en"

    # trainig paremeters
    replace_pronunciation_prob = 1.0
    outputs_per_step = 5
    batch_size = 60
    batch_split = int(batch_size*0.5)
    epochs = 2000
    guided_attention_ratio = 0.995
    teacher_forcing_ratio = 0.5
    attention_scale = 15
    attention_decay = 0.997