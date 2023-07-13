from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer


# Create your views here.

bot = ChatBot('chatchou', read_only=False, logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
           #default_response': 'Desolé les putes n ont pas les reponses a toutes les questions mon niveau d intelligence est tres limitée',
            #maximum_similarity_threshold': 0.90
        }
    ])

list_to_train = [
    "hi",
    "oui? je peux faire quelque chose pour toi?",
    "what's your name?",
    "je suis une petite pute de robot je n ai pas de nom",
    "what is your favorite food?",
    "j aime les uitres et les saucisses"
    
    ]
chatterbotcorpusTrainer= ChatterBotCorpusTrainer(bot)

#st_trainer = ListTrainer(bot)
#ist_trainer.train(list_to_train)

chatterbotcorpusTrainer.train("chatterbot.corpus.english")

def index(request):
    return render(request,'blog/index.html')

def specific(request):
    return HttpResponse("this is a requeest")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
