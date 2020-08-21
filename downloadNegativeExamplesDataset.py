
import sys
from lib import util

util.createDatasetFolderStructure()

util.downloadImagesFromGoogle(
    "meme template",
    "meme_tmpl",
    100,
    downloadpath="dataset/raw/meme",
)

util.downloadImagesFromGoogle(
    "person photography",
    "person_pht",
    150,
    downloadpath="dataset/raw/person",
)
