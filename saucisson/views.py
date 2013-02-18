from cornice import Service
import random
from datetime import datetime


saucisson = Service(name='saucisson', path='/')

MEMBERS = ('Etienne', 'Alexis', 'Vivien', 'Olivier', 'Paul', 'Arzhel', 'David',
           'Nical', 'Rik', 'Julien', 'Michal')


@saucisson.get()
def who(request):
    random.seed(datetime.now().timetuple()[:3])
    author = random.choice(MEMBERS)
    return "And the slicer is %s !" % author
