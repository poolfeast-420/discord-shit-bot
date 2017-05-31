from multiprocessing import Process, Event
from chatterbot import ChatBot
from words import vocabulary

class AI_Thread(Process):
    def __init__(self, send_queue, receive_queue):
        print('oawijfaof;a3r3qafisepfqw3fp92p9f')
        Process.__init__(self)
        self.shitbot = ChatBot(
            'shit bot',
            trainer='chatterbot.trainers.ListTrainer',
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
            #filters="chatterbot.filters.RepetitiveResponseFilter"
        )
        #self.shitbot.train(vocabulary['typing'])
        self.exit = Event()
        self.receive_queue = receive_queue
        self.send_queue = send_queue
        print('aojndio;andio;ani;dfeaifbitbfi;e')

    def run(self):
        print('ijwdoaw9diuao;iwdho;ajep9rd3')
        while not self.exit.is_set():
            message = self.receive_queue.get()
            new_message = self.shitbot.get_response(message)
            self.send_queue.put(new_message)

    def terminate(self):
        print('eoaduhawiourp9adp94nqwufndp923hr9wnof;ne')
        self.exit.set()
        self.receive_queue.close()

