from chattingtransformer import ChattingGPT2

def main():

    gpt2 = ChattingGPT2(model_name="gpt2")

    text = "On the first day of school I "



    results = gpt2.generate_text(text, method="greedy")
    print("greedy: ", results)
    print("----------------------------------------------------------------------------")
    results = gpt2.generate_text(text, method="beam-search")
    print("beam-search: ", results)

    print("----------------------------------------------------------------------------")

    results = gpt2.generate_text(text, method="generic-sampling")
    print("generic-sampling ", results)
    print("----------------------------------------------------------------------------")

    results = gpt2.generate_text(text, method="top-k-sampling")
    print("top-k-sampling: ", results)
    print("----------------------------------------------------------------------------")

    results = gpt2.generate_text(text, method="top-p-nucleus-sampling")
    print("top-p-nucleus-sampling: ", results)





if __name__ == "__main__":
    main()