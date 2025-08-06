from transformers import pipeline

def main():
    classifier = pipeline("sentiment-analysis")
    result = classifier("Pinokio makes local AI easy!")
    print(result)

if __name__ == "__main__":
    main()
