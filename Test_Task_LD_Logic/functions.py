import nv, nn
from datetime import datetime

class testScript(object):

    def __init__(self, name):
        self.name = name

    ### HELLO_LOGIC
    def hello(self):
        # play a hello script if get user voice go to hell_null prompt else go to hangup_null prompt
        with nv.listen() as r:
            nv.random_sound(2000, 7000)
            nv.say("""{}, good afternoon! You are concerned about Company X, we are conducting a survey of satisfaction with our services. \
            Tell me, is it convenient for you to talk now?""".format(self.name))
            self.hello_null()           
        self.hangup_null()

    def hello_repeat(self):
        nv.say("""This is Company X,  Tell me, is it convenient for you to talk now?""")
        self.recommend_main()

    def hello_null(self):
        nv.say("""Sorry, I can't hear you. Could you repeat please?""")
        # listen to user to get entities and there value
        with nv.listen(entities=["confirm", "wrong_time", "repeat") as r:
            if r.entity('confirm') == "true":
                self.recommend_main()
            elif r.entity('confirm') == "false":
                self.hangup_wrong_time()
            elif r.entity('wrong_time') == "true":
                self.hangup_wrong_time()
            elif r.entity('repeat') == "true":
                self. hello_repeat()
            else:
                pass

    ### MAIN_LOGIC
    def recommend_main(self):
        # play a recommend script if get user voice go to recommend_null prompt else go to hangup_null prompt
        with nv.listen() as r:
            nv.random_sound(2000, 7000)
            nv.say("""Tell me, are you ready to recommend our company to your friends? \
            Please rate it on a scale from "0" to "10", where "0" - I will not recommend it, "10" - I will definitely recommend it.""")
            self.recommend_null()
        self.hangup_null()

    def recommend_repeat(self):
        # play a recommend script if get user voice go to recommend_default prompt else go to hangup_null prompt
        with nv.listen() as r:
            nv.random_sound(2000, 7000)
            nv.say("""How would you rate the opportunity to recommend our company to your friends on a scale from 0 to 10, \
            where 0 - I will definitely not recommend it, 10-I will definitely recommend it.""") 
            self.recommend_default()
        self.hangup_null()

    def recommend_repeat_2(self):
        nv.say("""Well, if you were asked to recommend our company to friends, would you do it? If "yes" - then the score is "10", if exactly no - "0".""")
        # listen to user score
        with nv.listen(entities=["recommendation_score"]) as r:         
            if (r.entity('recommendation_score') >= 0) and (r.entity('recommendation_score') <= 8):
                self.hangup_negative()

    def recommend_socre_negative(self):
        nv.say("""Well, from 0 to 10, how would you rate: 0, 5 or maybe 7 ?""")
        # listen to user score
        with nv.listen(entities=["recommendation_score"]) as r:            
            if (r.entity('recommendation_score') >= 9):
                self.hangup_positive()

    def recommend_score_neutral(self):
        nv.say("""Well, from 0 to 10, how would you rate it ?""")
        # listen to user recommend intention
        with nv.listen(entities=["recommendation"]) as r:
            if r.entity('recommendation') == 'negative':
                self.recommend_socre_negative()

    def recommend_socre_positive(self):
        nv.say("""Well, on a 10-point scale, how would you rate 8-9 or maybe 10 ?""")
        # listen to user recommend intention
        with nv.listen(entities=["recommendation"]) as r:
            if r.entity('recommendation') == 'neutral':
                self.recommend_score_neutral()

    def recommend_null(self):
        nv.say("""I'm sorry I can't hear you, could you repeat that ?""")
        # listen to user recommend intention
        with nv.listen(entities=["recommendation"]) as r:
            if r.entity('recommendation') == 'positive':
                self.recommend_socre_positive()

    def recommend_default(self):
        nv.say("""I'm sorry I can't hear you, could you repeat that ?""")
        # listen to user to get entities and there value
        with nv.listen(entities=["repeat", "wrong_time", "question", "recommendation"]) as r:
            if r.entity('repeat') == "true":
                self.recommend_repeat()
            elif r.entity('recommendation') == 'dont_know':
                self.recommend_repeat_2()
            elif r.entity('wrong_time') == "true":
                self.hangup_wrong_time()
            elif r.entity('question') == "true":
                self.forward()
            else:
                pass

    ### HANGUP_LOGIC
    def hangup_positive(self):
        nv.say("""Great! Thank you so much for your time! All the best to you!""")
        return "High score"

    def hangup_negative(self):
        nv.say("""I understand you. In any case, thank you so much for your time! All the best to you.""")
        return "Low score"

    def hangup_wrong_time(self):
        nv.say("""I'm sorry to bother you. All the best to you""")
        return "No time to talk"

    def hangup_null(self):
        nv.say("""I can't hear you anyway, so I'd better call you back. All the best to you""")
        return "problems with understanding "

    def forward(self):
        return "transfer to the operator"

if __name__ == "__main__":
    ### initial a call
    nn.call('89001234567', '25-03-2020 01:00:00')
    ### call the logic script with argument name is user name
    test_script = testScript(name)