from flask import Flask
from flask_restful import Api, Resource
import wikipedia

app = Flask(__name__)
api = Api(app)

class ArtistSearch(Resource):
    def get(self, artist):
        actualartist = wikipedia.search(artist)[0]
        return wikipedia.summary(actualartist, sentences=5)

api.add_resource(ArtistSearch, "/artistsearch/<string:artist>")


if __name__ == "__main__":
    app.run(debug=True)