
import sys
from lib import util

util.createDatasetFolderStructure()

util.downloadImagesFromGoogle(
    "meme template",
    "meme_tmpl",
    None,
    None,
    "dataset/raw/negative",
)