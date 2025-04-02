import csv
from app import db, Sentence, app  # Import Flask app and models

def bulk_insert():
    with app.app_context():  # Ensure app context for DB operations
        with open("sentences.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            sentences = []
            for row in reader:
                hindi, english = row
                sentences.append(Sentence(hindi=hindi, english=english))

            db.session.bulk_save_objects(sentences)  # Bulk insert
            db.session.commit()
            print(f"{len(sentences)} sentences added successfully!")

if __name__ == "__main__":
    bulk_insert()
