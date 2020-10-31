
POSSIBLE_METHODS = ["greedy", "beam-search", "generic-sampling",
                    "top-k-sampling", "top-p-nucleus-sampling", "custom"]

DEFAULT_SETTINGS = {
    "do_sample": False,
    "early_stopping": False,
    "num_beams": 1,
    "temperature": 0.65,
    "top_k": 50,
    "top_p": 1.0,
    "repetition_penalty": 1,
    "length_penalty": 1,
    "no_repeat_ngram_size": 2,
    'bad_words_ids': None,
}


def __get_greedy_settings():
    return DEFAULT_SETTINGS.copy()


def __get_beam_settings():
    settings = DEFAULT_SETTINGS.copy()
    settings["num_beams"] = 5
    settings["early_stopping"] = True
    return settings


def __get_generic_sampling_settings():
    settings = DEFAULT_SETTINGS.copy()
    settings["do_sample"] = True
    settings["top_k"] = 0
    settings['temperature'] = 0.7
    return settings


def __get_top_k_sampling_settings():
    settings = DEFAULT_SETTINGS.copy()
    settings["do_sample"] = True
    settings['top_k'] = 50
    return settings


def __get_p_nucleus_sampling_settings():
    settings = DEFAULT_SETTINGS.copy()
    settings["do_sample"] = True
    settings['top_p'] = 0.92
    settings['top_k'] = 0
    return settings


def get_settings(method, custom_settings, logger):
    settings = {}
    if method == "greedy":
        settings = __get_greedy_settings()
    elif method == "beam-search":
        settings = __get_beam_settings()
    elif method == "generic-sampling":
        settings = __get_generic_sampling_settings()
    elif method == "top-k-sampling":
        settings = __get_top_k_sampling_settings()
    elif method == "top-p-nucleus-sampling":
        settings = __get_p_nucleus_sampling_settings()
    elif method == "custom":
        settings = get_custom_settings(custom_settings, logger)

    return settings

def get_custom_settings(custom_settings, logger):

    possible_keys = list(DEFAULT_SETTINGS.keys())
    settings = DEFAULT_SETTINGS.copy()

    for key, value in custom_settings.items():

        if key in possible_keys:
            settings[key] = value
        elif key == "min_length":
            logger.warning("\"min_length\" is now parameters for the generate_text method")
        elif key =="max_length":
            logger.warning("\"max_length\" is now parameters for the generate_text method")
        else:
            logger.warning("\"%s\" is not a valid argument", key)
    return settings
