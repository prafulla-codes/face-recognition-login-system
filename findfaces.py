import face_recognition

image = face_recognition.load_image_file("./img/groups/team2.jpg")

# to find co-ordinates of each face
face_locations = face_recognition.face_locations(image)
print(face_locations)

# to find no. of faces

print(f'There are {len(face_locations)} people in this image')