import streamlit as st
from PIL import Image
from pathlib import Path

# config

IMAGES=Path('images')
IMAGES.mkdir(exist_ok=True)

BACKUP=Path('backup')
BACKUP.mkdir(exist_ok=True)

"""# Enrollment"""

if st.checkbox("Use camera"):
    uploaded_file = st.camera_input('Take a selfie')
else:
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.")

    image_name = st.text_input('Enter the name for the image:', 'image_name.png')

    if st.button('Save Image'):
        image.save(IMAGES / image_name)
        image.save(BACKUP / image_name) # backup
        st.success(f'Image saved as {image_name}!')


"""# Gallery"""

"""List of known images"""

"""## Filter

Enter text to display only matching images. Leave empty to display all images.
"""

filter = st.text_input('Filter:', '')

"""## Enrolled"""


for _i in IMAGES.glob('*'):
    if filter and filter not in _i.name:
        continue
    image_path = Path(_i)
    # read
    image = Image.open(image_path)
    size = image.size
    # resize to 100x100:
    image.thumbnail((100, 100))
    st.image(image, caption=f"{image_path.name} ({size[0]}x{size[1]})")
    # button for removing image:
    if st.button(f"Remove {image_path.name}", key=image_path.name):
        image_path.unlink()
        st.success(f"Removed {image_path.name}!")





