__name__ = "vutsuak"

from tqdm import tqdm
from time import sleep

for i in tqdm(range(5)):
    sleep(.5)


# why is this module working only in command line , the IDE shows : name error cant import tqdm