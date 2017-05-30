from multiprocessing import Process, Event
from chatterbot import ChatBot

class AI_Thread(Process):
    def __init__(self, send_queue, receive_queue):
        print('Starting AI')
        Process.__init__(self)
        self.shitbot = ChatBot(
            'shit bot',
            trainer='chatterbot.trainers.ListTrainer',
            storage_adapter="chatterbot.storage.JsonFileStorageAdapter"
        )
        self.exit = Event()
        self.receive_queue = receive_queue
        self.send_queue = send_queue
        print('AI Loaded')

    def run(self):
        print('AI Running')
        while not self.exit.is_set():
            message = self.receive_queue.get()
            new_message = self.shitbot.get_response(message)
            self.send_queue.put(new_message)

    def terminate(self):
        print('AI Stopped')
        self.exit.set()
