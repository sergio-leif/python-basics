"""
Create a library of similar images with a list of different aspects or keywords, for example "blue-shirt" or "green-eyes". Each of the images has an ID which is unique in the library.

Every image will be scored according to the rarity of the image (if an image has not usual keywords/aspect it will have a better score).

Show the library of images in order, showing the images with better score in the top.

Indicate the best 2 images regarding a specific library

Example:

Library of images about "mountain":
- keywords: trees, snow, stones, lake, animals, etc

mountain_1:
 - id: 1
 - keywords: snow, trees, lake

mountain_2:
 - id: 2
 - keywords: trees, snow, stones

mountain_3:
 - id: 3
 - keywords: trees, snow, lake, stones, animals

The score of mountain_3 will be better (lower number is better), as it's the only one with animals
"""

# class Image:

#     def __init__(self, id, keywords, score="0"):
#         self.id = id
#         self.keywords = keywords
#         self.score = score

# image_1 = Image(1, ['trees', 'animals', 'snow'])
# image_2 = Image(2, ['animals', 'snow', 'stones'])
# image_3 = Image(3, ['lake', 'trees'])
# image_4 = Image(4, ['stones', 'trees'])

# mountain_1 = {'id': image_1.id, 'keywords': image_1.keywords, 'score': image_1.score}
# mountain_2 = {'id': image_2.id, 'keywords': image_2.keywords, 'score': image_2.score}
# mountain_3 = {'id': image_3.id, 'keywords': image_3.keywords, 'score': image_3.score}
# mountain_4 = {'id': image_4.id, 'keywords': image_4.keywords, 'score': image_4.score}

# # library['images'].update('key': image_1.get_id, 'keywords': image_1.get_keywords, 'score': image_1.score)
# # library['images'].update('key': image_2.get_id, 'keywords': image_2.get_keywords, 'score': image_2.score)
# # library['images'].update('key': image_3.get_id, 'keywords': image_3.get_keywords, 'score': image_3.score)
# # library['images'].update('key': image_4.get_id, 'keywords': image_4.get_keywords, 'score': image_4.score)

# library = [mountain_1, mountain_2, mountain_3, mountain_4]
# print(library)

# keywords = []
# for image in library:
#     keywords.extend(image['keywords'])

# scores = {}
# for keyword in set(keywords):
#     scores[keyword] = keywords.count(keyword)

# punctuations = sorted(scores.items(),key = lambda x:x[1])

# best_score = punctuations[0][0]
# print(best_score)

# for image in library:
#     if best_score in image['keywords']:
#         print(f"The image with better score has the ID: {image}")



class Image:
    def __init__(self, id, keywords):
        self.id = id
        self.keywords = keywords

library = [
    Image(1, ["snow", "trees", "lake"]),
    Image(2, ["trees", "snow", "stones"]),
    Image(3, ["trees", "snow", "lake", "stones", "animals"])
]

def calculate_score(image, keywords):
    uncommon_keywords = set(image.keywords) - set(keywords)
    return len(uncommon_keywords)

specific_keywords = ["animals"]  # Specify the keywords to find the best images
library.sort(key=lambda image: calculate_score(image, specific_keywords))

for image in library:
    print(f"Image ID: {image.id}, Score: {calculate_score(image, specific_keywords)}")

best_images = library[:2][0].id

print(f"Best images are: {best_images}")