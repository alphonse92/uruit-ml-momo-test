
import sys
from lib import util

util.createDatasetFolderStructure()
#util.createDatasetFolderStructure()(
#     "momo",
#     "momo_",
#     50,
# )
#util.createDatasetFolderStructure()(
#     "momo terror",
#     "momo_terror_",
#     50,
# )

#util.createDatasetFolderStructure()(
#     "momo whatsapp",
#     "momo_wsp",
#     10,
# )

#util.createDatasetFolderStructure()(
#     "momo video",
#     "momo_video",
#     10,
# )

#util.createDatasetFolderStructure()(
#     "momo noticias",
#     "momo_noticias",
#     10,
# )

#util.createDatasetFolderStructure()(
#     "momo historia",
#     "momo_historia",
#     10,
# )

util.downloadImagesFromGoogle(
    "momo historia",
    "momo_historia",
    10,
    downloadpath="dataset/raw/",
    chromedriver="/usr/local/bin/chromedriver"
)



