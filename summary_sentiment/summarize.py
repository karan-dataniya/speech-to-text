# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#model_dict = "MEETING_SUMMARY"
import torch 


class Model():

    def __init__(self,model_dict):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dict)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_dict)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # self.tokenizer.to(self.device)
        # self.model.to(self.device)

    def clean_text(self,text,num=450):
        run = len(text)/num
        a = 0
        b = 500
        txt_ = []
        for i in range(0,int(run)):
            txt_.append(text[a:b])
            a = b
            b += 500
        return txt_
        
    def summary(self,txt_):
        final_sum = []
        for input_text in txt_:
            # Tokenize input text
            inputs = self.tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True,padding=True)
            
            # Generate output summary
            output = self.model.generate(**inputs,
                max_length=700,  # Set the desired max length for the output
                num_beams=4,    # Adjust the number of beams for beam search
                temperature=0.8,  # Adjust the temperature for sampling (for models that support it)
                top_k=50,       # Adjust the top-k parameter for sampling (for models that support it)
                top_p=0.9)

            # Decode and print the generated summary
            generated_summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            final_sum.append(generated_summary)
            # print("Generated Summary:")
            # print(generated_summary)
        return ''.join(final_sum)

if __name__ == "__main__":
    txt = """
    "Speaker 0: Speaker 1: Hi, I just got a call from this number. Speaker 0: Yes. Speaker 1: May I know your good name? Speaker 0: Marion King, Mr. Paul. Speaker 1: Oh yes, I called you on your another number. I think this is another number. That is why I cannot. Speaker 0: Okay. Speaker 1: Okay. Okay. Hi, Marion. This is Shobik. I am from Arkin Staffing, basically, and I actually, you know, got your profile that is from monster.com, the job board, and I have an excellent job opportunity for you that is as a director of risk management. So, just, you know, wanted to check if you are looking for any kind of a job opportunity. Speaker 0: I actually am. I was just waiting, you know, looking for the right opportunities, there is so much out here. Oh my goodness. Yes, sir. Now, where is this located geographically? Speaker 1: So this position, it is an on-site position, and it is located in Middletown, Delaware. Speaker 0: Oh, okay. That is not, I mean, it is not next door, but it is not too far there. Speaker 1: Great. Yes. So let me tell you a little bit about the job position first. So this position, as I told you, the title is the director of risk management, and this is a full-time opportunity that one of our direct client name is Bizav International. Speaker 0: Can you say that once more? Speaker 1: It is Bizav. It is B-I-Z-A-V. Bizav. Okay. Gotcha. Okay. Speaker 0: I thought I said, well, maybe I am missing something, but I understand. Okay. Speaker 1: No problem. So this is actually an aviation and aircraft service provider company. And they want somebody who have great experience with the risk management, risk control, basically the operational risk management experience, who can make these strategies, make the models of the risk management for the firm, and who have experience or proficiency in maybe in C or C++ or MATLAB or SAS. Right? Speaker 0: Yeah. I do not want a program. I used to do that years ago. Speaker 1: It is a kind of a preferred skill, but it is not really required. But majorly, they want somebody with the risk management in the information security side and also who have experience with some of the networking part. Speaker 0: Yes. Now, I work for Comcast for years in networking and engineering. I come from networking and engineering background for like six, seven years. And then I moved over into the security and controls and GRC and a whole lot of different access management, the whole security game. And actually, I just recently, July, I obtained my CISSP. And I do not mind doing hands-on stuff, but not program. I cannot. Now, is SQL or something like that, sure, and I am also SQL certified, but going back in the, and I did quite well with, it is funny that, but that stuff drives you to drinking. Right. Speaker 1: Great. Speaker 0: Great. Yeah. That is like two different though, but that is kind of like two different jobs. doing programming and risk management is like they are asking for two different jobs in one. Speaker 1: So here I wanted to interview, sorry about that. But the, as I told you, the, this is basically a directed position, so you do not have to do the hands-on things, but, you know, this is actually a preferred, you know, experience what they are looking for. If you have in, in, in your, you know, previous background or previous companies, basically, but they are mostly focusing on the risk management part, information security and the networking side experience. These are the, yeah, yeah. So this is what we are actually looking for. And your profile, you know, looks that you have been, you know, into the risk management and compliance security and everything you have, right. So I can, I just wanted to know, like, in, in, in Monster, I can see that the last project you have done with JP Morgan, Jesus. So is this the updated resume or like after this project, you have bought anywhere? Speaker 0: No, no, no. It actually is. I just took time off to get, to go in and tackle the CISSP. I am so happy I have had first try. And then I kind of took the summer off because I was, you know, just tired. So I said, let me enjoy the summer and now I am ready to get back to work. So I am back in the market now. Speaker 1: So this was your last project with JV Chases? Speaker 0: Correct. Okay. Speaker 1: All right. So, Marianne, if you got selected for this role, so how soon you can be able to join? Speaker 0: Monday. Oh, okay. Great. Speaker 1: Thank you. Speaker 0: Yeah. I am free right now. So I am going to be able to start. Okay. Speaker 1: So may I know, like, what is your expectation about the salary? Speaker 0: Well, you said it is a risk director position. Yeah. I would say probably around 150 somewhere in that area. Speaker 1: Okay. But, you know, for this role, I can give you like 140K. This is the maximum I can, you know. Speaker 0: Okay. Well, I mean, yeah. I mean, there is a lot of times some companies, they do not have as much, let us say, money to distribute it as others. Speaker 1: But the market is also, you know, currently it is not that good too. Speaker 0: And it is kind of weird right now. I think, you know, that is why I said I was not killing myself when the right thing comes along that I have come along. But I am like, I do not, it is just, I was just saying, and at first I thought it was me and I asked a few people. I am like, is it my resume? They are like, no, it is the market. Exactly. You see all these jobs out there and they are like, they have the jobs out there, but they are really not hiring. I am like, right. Yeah, it does not make sense. But for somebody, I guess that is where they are going. Speaker 1: Right. Speaker 0: Yes. Speaker 1: Mm hmm. Okay. Sounds really great. So I just, you know, wanted to share you the rate agreement email and I just need your acknowledgement on that. So right to represent. Right to represent. Yes. Right to represent. And this is our direct line basically. And I, you know, once I have your acknowledgement, my manager, I will, I will share your profile to my manager and she will going to share your resume to the hiding manager's desk. And after that, you know, if we have anything scheduled for next week, I probably it will be, it will take one or two days to, you know, shortlist and everything. And most probably by, by the Monday, they will get back to us and I will get back to you and let you know what is the feedback. Okay. Speaker 0: And please feel free to do that. Like, I do not think it is your fault. I mean, if they say, well, we want someone a little taller, we want to, you know, that is not, you know, I would not be mad at you when you say, hey, did you decide to go with a different candidate? That is fine. They have that right. It is their job. Please feel free to do that, you know, because I hate when you, people reach out to you and then they never get back to you because sometimes we keep ourself on hold. If you say next week, I was like, okay, well, I am waiting for him to get back to me. And it is only fair, you know, both ways that week. Absolutely. Speaker 1: Do not worry about that. I just, you know, shared you the email to you. Do you have your email access right now? Speaker 0: I do. Yeah. Speaker 1: I can check. Did you receive it or not? Speaker 0: Yeah, I did receive it. Yes, sir. Mm hmm. All right. So I think, I think, I think this one is the, okay. Now I got it. Give me one second. I am going to recline. Now, let me ask you this, do they pay every week or every two weeks do you know? Speaker 1: I exactly, I am not sure about it, but I can, you know, tell my manager to ask them about it. Speaker 0: Okay. But I was just, you know, just wondering, oh, no problem. Speaker 1: Okay. Speaker 0: So I am almost done. Speaker 1: Okay. Speaker 0: Do you have another copy of my resume? Speaker 1: If you can attach the copy, that would be great. Okay. Yeah. Speaker 0: I will definitely do that. Give me one second. Okay. I am almost done. Speaker 1: Okay. Speaker 0: Okay. Okay. Oh, for crying out loud. I apologize. You have no problem. I was looking in the wrong folder. Okay. Okay. Okay. Okay. Okay. Okay. Okay. Speaker 1: Okay. Okay. Speaker 0: Okay. I am looking in the wrong folder. Okay. Speaker 1: Oh, did it attach? Speaker 0: So, we, let me see if it does. Oh, okay. Okay. Okay. Okay. Okay. Okay, I am sorry. I am sorry. Okay. Speaker 1: Oh, okay. Okay. Okay. Okay. Okay. Okay. Okay. Okay. Okay. Okay. Speaker 0: Okay. Okay. Okay. Okay. Okay. Okay. Okay. hmm for some reason I think it attacked so I am going to resend it all right. I just sent it back to you. so okay I guess you can give me a call. I you know. give me in some direction when ever you get any answers from them. Speaker 1: absolutely absolutely I will definitely let you know about it. and this is your location 600 and Broad Street suit 5 Middletown. no I am actually in New Jersey. Speaker 0: I am about an hour away but I am used to commuting to Delaware. I have worked over there before for years. okay actually Jackie Morgan was in Delaware. Speaker 1: oh okay got it got it not an issue then. so I just you know received your acknowledgement but there is no attachment in it. Speaker 0: oh I think you are not one with the attachment. oh get that second. Speaker 1: okay okay no problem it is you know I I did you know make sure that I will do my best to get the interview process. and also you know this company is also very good company so you will really enjoy working with them if you got selected. so hope for the bit hope for the best and yeah all right all right thank you so much I appreciate thank you Marianne. thank you I really enjoy talking to you and we will talk to you soon. Speaker 0: right absolutely all righty. thank you again. thank you yep bye-bye."
    """
    
    model = Model('summary_sentiment/MEETING-SUMMARY-BART-LARGE-XSUM-SAMSUM-DIALOGSUM-AMI')
    
    clean = model.clean_text(txt)
    print(model.summary(clean))