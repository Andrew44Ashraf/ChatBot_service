from mongoengine import *

connect('ADDRESS TO BE DETERMINED')

class Cluster(Document):
  user_token = StringField(required=True)
  tag = StringField(required=True)
  patterns = StringField(required=True)
  responses = StringField(required=True)

class Token(Document):
  token = StringField(required=True)
  
def save_cluster(token, tag, patterns, responses):
  cluster = Cluster(user_token=token, tag=tag, patterns=patterns, responses=responses)
  cluster.save()


def get_clusters(token, tag=''):
  if tag != '':
    clusters = Cluster.objects(user_token=token)
  else:
    clusters = Cluster.objects(user_token=token, tag=tag)

  return clusters


def delete_cluster(token, tag):
  cluster = Cluster.objects(user_token=token, tag=tag).first()
  cluster.delete()


def save_token(token):
  token = Token(token=token)
  token.save()

def token_exists(token):
  if Token.objects(token=token):
    return True

  return False