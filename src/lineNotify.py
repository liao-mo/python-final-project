import requests


HANK_API_KEY = "L5ndN5HrN07x8RQkJ03znyCOzGfLIQ3FSFkZdT3SoWo"
BRIAN_API_KEY = "8jxKWOdikn1dwNR8jejCyYk0iHYEhTQz2ZyujEgvXWK"  # added
GROUP_API_KEY = "aXeGGuxXR4KFNZlMXg0yfvIwD2ledWRD3mQI0L2Sume"


class LineNotify:
    def __init__(self, api_key=BRIAN_API_KEY) -> None:
        self.base_url = "https://notify-api.line.me/api/notify"
        self.header = {"Authorization": f"Bearer {api_key}"}

    def send_image(self, image_path, description):
        try:
            # Open the image file in binary mode
            with open(image_path, "rb") as image_file:
                # Create a dictionary with the form data
                api_endpoint = self.base_url + f"?message={description}"
                files = {"imageFile": (image_path, image_file, "image/png")}
                # Make a POST request with the image file as form data
                response = requests.post(api_endpoint, headers=self.header, files=files)

            # Check the response
            if response.status_code == 200:
                print("Image uploaded successfully!")
            else:
                print(f"Error uploading image. Status code: {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"Error: {e}")

    def send_message(self, message):
        try:
            api_endpoint = self.base_url + f"?message={message}"

            # Make a POST request
            response = requests.post(api_endpoint, headers=self.header)

            # Check the response
            if response.status_code == 200:
                print("Message uploaded successfully!")
            else:
                print(f"Error sending image. Status code: {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"Error: {e}")
