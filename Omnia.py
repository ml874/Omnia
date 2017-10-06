import wolframalpha
import wikipedia
import os
import loginkeys as login


say = 'say '


def question():
    while True:
        question = raw_input("Question: ")
        try:
            # Wolfram Alpha
            app_id = login.WOLFRAM_KEY
            client = wolframalpha.Client(app_id)
            result = client.query(question)
            result = next(result.results).text
            print result
            os.system(say + str(result))
        except:
            # Wikipedia
            print wikipedia.summary(question, sentences=1)
            result = wikipedia.summary(question, sentences=1)
            print type(result)
            result = str(result)
            os.system(say + result)


def query(input):

    try:
        # Wikipedia
        print wikipedia.summary(input, sentences=1)
        result = wikipedia.summary(input, sentences=1)
        print type(result)
        result = str(result)
        os.system(say + result)
    except:
        pass
        # Wolfram Alpha
        app_id = login.WOLFRAM_KEY
        client = wolframalpha.Client(app_id)
        result = client.query(input)
        result = next(result.results).text
        print result
        os.system(say + str(result))
