from chattingtransformer import ChattingGPT2

def main():

    gpt2 = ChattingGPT2("gpt2")

    text = "I think therefore I  "

    default_settings = {
        "min_length": 2,
        "do_sample": False,
        "early_stopping": False,
        "num_beams": 1,


    }
    results = gpt2.generate_text(text, method="custom", custom_settings=default_settings)
    print(text)
    print(results)


if __name__ == "__main__":
    main()