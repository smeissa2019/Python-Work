%reload_ext autoreload
%autoreload 2
%matplotlib inline

from fastai import *
from fastai.vision import *

path = untar_data('TwitterArtBot\yalefaces') 
path.ls()

