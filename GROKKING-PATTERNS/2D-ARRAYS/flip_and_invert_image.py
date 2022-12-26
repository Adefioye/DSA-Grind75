from typing import List 

image1 = [[1,1,0],[1,0,1],[0,0,0]]  #  [[1,0,0],[0,1,0],[1,1,1]]
image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] #    [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:

    # Reverse each row
    # Invert each row and add to a new array
    new_image = []

    for img in image:
        img = img[::-1]

        inv_img = []
        for item in img:
                
            if item == 0:
                inv_img.append(1)
            else:
                inv_img.append(0)
            
        new_image.append(inv_img)

    return new_image



def optimalFlipAndInvertImage(image: List[List[int]]) -> List[List[int]]:

    # To reduce the reverse and invert step

    for img in image:
        l = 0
        r = len(img) - 1

        while l <= r:

            if img[l] == img[r]:
                img[l] = 1 - img[l]
                img[r] = img[l]
                
            l += 1
            r -= 1


    return image

# print(flipAndInvertImage(image1))
# print(flipAndInvertImage(image2))

print(optimalFlipAndInvertImage(image1))
print(optimalFlipAndInvertImage(image2))