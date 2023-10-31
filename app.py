from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string


def image_to_sound(path_to_image, target_language="en"):
    """
    Function for converting an image to sound
    Args:
        path_to_image (str): Path to the image file.
        target_language (str): Target language code or name. Default is "en".
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)

        # Ensure the target language is valid
        available_languages = gTTS.LANGUAGES.keys()
        if target_language not in available_languages:
            print(f"Error: Language '{target_language}' is not supported.")
            return False

        sound = gTTS(cleaned_text, lang=target_language)
        sound.save("sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code\n", bug)
        return False


if __name__ == "__main__":
    # Call the function with the target language code or name (e.g., "fr" for French)
    image_to_sound("image.jpg", target_language="fr")
    input()
