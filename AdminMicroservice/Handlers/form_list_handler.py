import json
import psycopg2
from Database.db_handler import DatabaseHandler
from Config.config import get_config

class FormListHandler:
    @staticmethod
    def format_response(rez):
        forms = []
        for i in rez:
            forms.append(
                {"id":i[0], "title":i[1], "public":i[2], "image":i[3], "status":i[4], "questions":i[5],"nr_questions":len(i[5]["questions"]),"nr_responses":i[6], "description":i[5]["description"]}
            )
        return forms

    @staticmethod
    def handle_form_list(handler):
        user_id = (handler.path.split("/users/")[1])[0:16]
        print("User id: '"+user_id+"'")
        
        forms_of_user = []
        where_clause = ""
        
        if handler.path.find("?") != -1:
            qstr = handler.path.split("?")[1]
            for i in qstr.split("&"):
                print(i)
                #if i in {"public","public=true"}:
                #    conditions.append("public=true")
                if i == "filter=draft":
                    where_clause = " AND status='draft'"
                elif i == "filter=active":
                    where_clause = " AND status='active'"
                elif i == "filter=closed":
                    where_clause = " AND status='closed'"

                else:
                    # Daca intalnesc un parametru necunoscut
                    handler.send_json_response([])
                    return

        config = get_config()

        db_config = config['database']        
        db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])
        
        forms_of_user = FormListHandler.format_response(
            db.fetch_query("""SELECT id, name, public, image, status, questions, total_responses(id) FROM forms WHERE id_creator = %s""" + where_clause + ";", (str(user_id),))
            )

        handler.send_json_response(forms_of_user)
        
    @staticmethod
    def handle_explore_form_list(handler):
        forms_of_user = []
        where_clause = ""
        
        if handler.path.find("?") != -1:
            conditions = []
            qstr = handler.path.split("?")[1]
            for i in qstr.split("&"):
                print(i)
                if i in {"public","public=true"}:
                    conditions.append("public=true")
                elif i == "filter=draft":
                    conditions.append("status='draft'")
                elif i == "filter=active":
                    conditions.append("status='active'")
                elif i == "filter=closed":
                    conditions.append("status='closed'")


                else:
                    # Daca intalnesc un parametru necunoscut
                    handler.send_json_response([])
                    return
                

            if len(conditions) > 0:
                where_clause = " AND " + " AND ".join(conditions)
        print(where_clause)
        config = get_config()

        db_config = config['database']        
        db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])
        
        forms_of_user = FormListHandler.format_response(
            db.fetch_query("""SELECT id, name, public, image, status, questions FROM forms WHERE public = true AND status = 'active'""" + where_clause + " LIMIT 10;")
        )
        handler.send_json_response(forms_of_user)

    @staticmethod
    def handle_delete_form(handler):
        form_id = handler.path.split("/forms/")[1][0:16]
        config = get_config()

        db_config = config['database']        
        db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])
        
        db.cursor.execute("""DELETE FROM forms WHERE id = %s;""", (str(form_id),))
        if(db.cursor.rowcount > 0):
            db.connection.commit()
            handler.send_response(200)
            handler.end_headers()
        else:
            db.connection.rollback()
            handler.send_response(409) #Conflict
            handler.end_headers()

    def handle_update_form(handler):
        content_length = int(handler.headers['Content-Length'])
        patch_data = handler.rfile.read(content_length)
        patch_data_decoded = patch_data.decode('utf-8')
        patch_data_json = json.loads(patch_data_decoded)
        
        newStatus = None
        
        for i in patch_data_json:
            if i == "status":
                if patch_data_json[i] in {"active", "closed"}:
                    newStatus = patch_data_json[i]
        
        if newStatus:
            form_id = handler.path.split("/forms/")[1][0:16]
            config = get_config()

            db_config = config['database']        
            db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])
            db.cursor.execute("""UPDATE forms SET status=%s WHERE id = %s;""", (str(newStatus),str(form_id),))
            if(db.cursor.rowcount > 0):
                db.connection.commit()
                handler.send_response(200)
                handler.end_headers()
            else:
                db.connection.rollback()
                handler.send_response(409) #Conflict
                handler.end_headers()
