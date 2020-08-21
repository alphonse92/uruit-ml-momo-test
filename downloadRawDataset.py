
import sys
from lib import util

util.createDatasetFolderStructure()
response = util.downloadImagesFromGoogle(
    "momo",
    "momo_",
    50,
)
response = util.downloadImagesFromGoogle(
    "momo terror",
    "momo_terror_",
    50,
)

response = util.downloadImagesFromGoogle(
    "momo whatsapp",
    "momo_wsp",
    10,
)

response = util.downloadImagesFromGoogle(
    "momo video",
    "momo_video",
    10,
)

response = util.downloadImagesFromGoogle(
    "momo noticias",
    "momo_noticias",
    10,
)

response = util.downloadImagesFromGoogle(
    "momo historia",
    "momo_historia",
    10,
)



