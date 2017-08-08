import cProfile

from Products.Five.browser import BrowserView

class Profiler(BrowserView):
    def __init__(self, context, request):
        super(Profiler, self).__init__(context, request)
        self.pr = cProfile.Profile()
        self.outfile = "profile-stats"
        
    def start(self, filename=None):
        if filename is not None:
            self.outfile = filename
            
        self.pr = cProfile.Profile()
        self.pr.enable()
        
    def stop(self):
        self.pr.disable()
        self.dump_stats()
        
    def dump_stats(self):
        self.pr.dump_stats(self.outfile)
        
    