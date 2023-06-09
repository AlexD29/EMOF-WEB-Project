from Helpers.json_response import JsonResponse
import json
import psycopg2

class ExploreListHandler:
    select_skeleton = """SELECT f.id, f.name, image, questions, total_responses(f.id), u.username, f.published_at, f.closed_at
            FROM forms f JOIN users u ON u.id = id_creator WHERE status='active' AND public=TRUE"""
    @staticmethod
    def format_response(cursor):
        rez = cursor.fetchall()
        forms = []
        for i in rez:
            forms.append(
                {"id":i[0], "title":i[1], "image":i[2],
                 "questions":i[3],"nr_questions":len(i[3]["questions"]),"nr_responses":i[4], "description":i[3]["description"], "author":i[5]}
            )
        return forms

    @staticmethod
    def handle_popular(handler):
        forms = []
        conn = psycopg2.connect(
                    host="localhost",
                    user="EMOF",
                    password="EMOF123_",
                    database="EMOF")
        cursor = conn.cursor()
        cursor.execute(ExploreListHandler.select_skeleton + """ ORDER BY total_responses(f.id) DESC LIMIT 10;""")
        forms = ExploreListHandler.format_response(cursor)
        cursor.close()
        conn.close()
        print(len(forms))

        handler.send_json_response(forms)

    
    @staticmethod
    def handle_new(handler):
        forms = []
        conn = psycopg2.connect(
                    host="localhost",
                    user="EMOF",
                    password="EMOF123_",
                    database="EMOF")
        cursor = conn.cursor()
        cursor.execute(ExploreListHandler.select_skeleton + """ ORDER BY f.published_at DESC LIMIT 10;""")
        forms = ExploreListHandler.format_response(cursor)
        cursor.close()
        conn.close()

        handler.send_json_response(forms)