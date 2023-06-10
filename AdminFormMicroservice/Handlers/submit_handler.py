import json
import secrets

from Config.config import get_config
from Database.db_handler import DatabaseHandler
from Helpers.json_response import JsonResponse

class SubmitHandler:
    @staticmethod
    def handle(handler):

        #if id is None:
        #    handler.send_json_response(JsonResponse.error("Form ID is empty") , 400 )
        #    return

        #TODO : ADD SOME MORE VERIFICATION HERE

        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        post_data_decoded = post_data.decode('utf-8')
        post_data_json = json.loads(post_data_decoded)
        
        print(json.dumps(post_data_json, indent=4))  # Afiseaza datele JSON într-un format lizibil

        config = get_config()

        db_config = config['database']        
        db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])

        #TO BE DELETED
        user_id = "2kwlJ6PpobfKYvQo"
        name = post_data_json.pop("name")
        tags = post_data_json.pop("tags")
        form_id = secrets.token_hex(16)[:16] 

        form_data = {
            'id': form_id,
            'id_creator': user_id, 
            'name': name,
            'questions': post_data_json,  
            'public': True,  # presupunem că formularul este public
            'published': False,  # presupunem că formularul este publicat
        }

        print("ASTA E JSONU FORM_DATA CE URMEAZA SA INTRE IN DB :")
        print(form_data)
         # inserați datele în baza de date
        query = """
        INSERT INTO public.forms 
        (id, id_creator, name, created_at, questions, public, published)
        VALUES (%s, %s, %s, NOW(), %s, %s, %s)
        """
        db.execute_query(query, (form_data['id'], form_data['id_creator'], form_data['name'], 
                                 json.dumps(form_data['questions']), form_data['public'], form_data['published']))

        # Trimiterea raspunsului
        handler.send_json_response(JsonResponse.success("Data received and processed"))
