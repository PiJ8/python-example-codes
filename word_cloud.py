from matplotlib import pyplot
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image

### File Processing ###
# Open and read the text file
with open("wordcloud.txt", "r", encoding="utf-8") as file:
    # Read the content of the file
    file_content = file.read()

# Split the content into words
word_array = file_content.split()

# Display the array of words
print(word_array)

### Word Cloud Generation ###
result = word_array
word_cloud_text = ''

for i in result:
    word_cloud_text = word_cloud_text + i + ' '

# Wording wished not to appear on word cloud
STOPWORDS.update(["see", "common"])

# Image used as mask, else the wordcloud by default will be a square size
mask = np.array(Image.open("mask_image.png"))
color= ImageColorGenerator(mask)

# Word cloud based on mask, final output will be based on image mask pixel size
wordcloud = WordCloud(width=3800, height=3800, max_words=1000, mask=mask, stopwords=STOPWORDS, background_color="white", random_state=42).generate(wordcloudtext)

# Simple word cloud
#wordcloud = WordCloud(background_color='white').generate(word_cloud_text)

# Output the wordcloud via savefig and imshow
# show
pyplot.figure(figsize=(38,38))
pyplot.imshow(wordcloud, interpolation='bilinear')
pyplot.axis("off")
pyplot.show()
pyplot.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')
