import pg8000
#pip3 install pg8000

conn = pg8000.connect(host="172.22.80.39", ssl=True,
                      user="itt385",
                      password="student",
                      database="itt385")
