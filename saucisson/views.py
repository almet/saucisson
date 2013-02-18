from cornice import Service

import json
import random
from datetime import datetime


saucisson = Service(name='saucisson', path='/')
slicers = Service(name='slicers', path='/slicers')
slicer = Service(name='slicers', path='/slicers/{name}')

SLICERS = ['etienne', 'alexis', 'vivien', 'olivier', 'paul', 'arzhel', 'david',
           'nical', 'rik', 'julien', 'michal']


@saucisson.get()
def who(request):
    random.seed(datetime.now().timetuple()[:3])
    author = random.choice(SLICERS)
    return "And the slicer is %s !" % author.capitalize()


@slicer.delete()
def remove_slicer(request):
    name = request.matchdict['name']
    if name.lower() in SLICERS:
        SLICERS.remove(name.lower())
        request.response.status = "204 THERE IS NO MORE"
        return "ok"
    else:
        request.response.status = "404 SORRY MATE"
        return "nope"


@slicers.post()
def add_slicer(request):
    try:
        name = json.loads(request.body).lower()
    except ValueError:
        request.errors.add('name', 'body', 'should be a JSON object')
        return "DAMN."

    if name not in SLICERS:
        SLICERS.append(name)
        request.response.status = "201 MOAR"
        created = request.application_url + slicer.path.format(name=name)
        request.response.headers['location'] = created
        return {'name': name}
    else:
        request.errors.status = 409
        request.errors.add('name', 'body', 'this slicer is already slicing')


@slicers.get()
def list_slicers(request):
    return {'slicers': SLICERS}
