import face_recognition

image_of_chester = face_recognition.load_image_file("./img/known/chester-bennington.jpg")

chester_face_encoding = face_recognition.face_encodings(image_of_chester)[0] #get Facial feature attribute

unknown_image = face_recognition.load_image_file("./img/unknown/chester.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0] #get facial feature attribute

# Compare Faces

results = face_recognition.compare_faces([chester_face_encoding],unknown_encoding)
if(results[0]):
    print("this is chester")
else:
    print("This is not chester")