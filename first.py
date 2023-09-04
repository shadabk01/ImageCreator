# importing openai module
import openai
import requests
from PIL import Image

# assigning API KEY to the variable

openai.api_key = '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'


# function for text-to-image generation
# using create endpoint of DALL-E API
# function takes in a string argument
def generate(text):
  res = openai.Image.create(
    # text describing the generated image
    prompt=text,
    # number of images to generate
    n=1,
    # size of each generated image
    size="256x256",
  )
  # returning the URL of one image as
  # we are generating only one image
  return res["data"][0]["url"]

# prompt describing the desired image
text = "batman art in red and blue color"
# calling the custom function "generate"
# saving the output in "url1"
url1 = generate(text)
# using requests library to get the image in bytes
response = requests.get(url1)
# using the Image module from PIL library to view the image
Image.open(response.raw)


response = requests.get(url1)
# saving the image in PNG format
with open("img.png", "wb") as f:
  f.write(response.content)
# opening the saved image and converting it into "RGBA" format
# converted image is saved in result
result = Image.open('img.png').convert('RGBA')
# saving the new image in PNG format
result.save('img_rgba.png','PNG')

# editing image using create_edit endpoint of DALL-E API
response = openai.Image.create_edit(
    # opening original image in read mode
    image=open("/content/img_rgba.png", "rb"),
    # opening mask image in read mode
    mask=open("/content/mask.png", "rb"),
    # propmt describing the desired image
    prompt="gotham city skyline behind batman",
    # number of images to be generated
    n=3,
    # size of each generated image
    size="256x256"
)
# saving the URLs of all image in new variable "res"
res = response['data']

# loop to save and display images
for i in range(len(res)):
    # saving URL of image in res
    image_url = res[i]['url']
    # extracting image from URL in bytes form
    response = requests.get(image_url, stream=True)
    # opening the image
    k = Image.open(response.raw)
    # displaying the image
    k.show()
    # saving the image
    with open(f"img_variant_{i}.png", "wb") as f:
        f.write(response.content)

        # using create_edit endpoint of the DALL - E API
        response = openai.Image.create_edit(
            # opening original image in read mode
            image=open("img_rgba.png", "rb"),
            # opening mask image in read mode
            mask=open("mask.png", "rb"),
            # text prompt describing the new image
            prompt="gotham city skyline behind batman",
            # number of images to be generated
            n=1,
            # size of each image generated in pixels
            size="256x256"
        )

        # saving the URLs of all image in new variable "res"
        res = response['data']

        # loop to save and display images
        for i in range(len(res)):
            # saving URL of image in res
            image_url = res[i]['url']
            # extracting image from URL in bytes form
            response = requests.get(image_url, stream=True)
            # opening the image
            k = Image.open(response.raw)
            # displaying the image
            k.show()
            # saving the image
            with open(f"img_mask_edit_{i}.png", "wb") as f:
                f.write(response.content)
