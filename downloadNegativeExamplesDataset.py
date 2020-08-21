
import sys
from lib import util

util.createDatasetFolderStructure()

# util.downloadImagesFromGoogle(
#     "meme template",
#     "meme_tmpl",
#     100,
#     downloadpath="dataset/raw/negative",
# )

util.downloadImagesFromGoogle(
    "person photography",
    "person_pht",
    2,
    downloadpath="dataset/raw/lala",
)
