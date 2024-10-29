from fileprocess import *

# because the original url of the task is hidden, we have to download and upload it elsewhere,
# I used google drive for that purpose.
# then gave the function our own url, just for doing this task.

downloaded = downloading('https://drive.google.com/uc?id=1h8EBKp_psYCq-Xjt4lzueZJqdUJoSRX9')

unzipped = unzip(downloaded)

opened = opening(unzipped)

read_write(opened)

# i made it much harder and longer than necassery! 
# but i wanted to make a reusable module and have costumized exceptions.