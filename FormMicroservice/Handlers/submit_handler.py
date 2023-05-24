from Helpers.json_response import JsonResponse
import json

class SubmitHandler:
    @staticmethod
    def handle(handler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        post_data_decoded = post_data.decode('utf-8')
        post_data_json = json.loads(post_data_decoded)
        
        print(json.dumps(post_data_json, indent=4))  # Afiseaza datele JSON într-un format lizibil

        # Trimiterea raspunsului
        handler.send_json_response(JsonResponse.success("Data received and processed"))
