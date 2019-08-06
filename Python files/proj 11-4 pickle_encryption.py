import shelve
import pickle

db = shelve.open(r"C:\Users\labuser\Desktop\simple-db.db")

m = { "first" : "lee" , "last" : "finn", "email" : "lee.finn@maine.edu" }

db["finn"] = pickle.dumps(m)

mm = pickle.loads(db["finn"])

db.close()
