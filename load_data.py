import os
import json
from pathlib import Path
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def get_duplicate_key_error_log(count):
    if count:
        return f"{count} ❗"
    else:
        return count


print('🚀🚀🚀 process started 🚀🚀🚀')

# MongoDB connection details
mongo_uri = "mongodb://root:123@localhost:27017/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Path to the workspace folder - (Current Folder)
BASE_DIR = Path(__file__).resolve().parent
workspace_path = str(BASE_DIR)


# Get a list of folders starting with "sample_*"
sample_folders = [folder for folder in os.listdir(workspace_path) if folder.startswith("sample_")]

if sample_folders:
    folders_list = '\n🔴 ' + '\n🔴 '.join(sample_folders) + '\n ==============================================\n\n'
    print(f"""\n\nThese are all the folder is going to load\n  {folders_list}""")
    
    for folder in sample_folders:
        folder_path = os.path.join(workspace_path, folder)
        
        # Create a database with the folder name
        db = client[folder]
        
        try:
            # Iterate over each file in the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".json"):
                    file_path = os.path.join(folder_path, file_name)
                    
                    # Create a collection with the file name
                    collection_name = os.path.splitext(file_name)[0]
                    collection = db[collection_name]
                    
                    # Insert documents into the collection
                    with open(file_path, "r") as file:
                        count = 0
                        success_count = 0
                        duplicate_key_error = 0
                        for line in file:
                            document = json.loads(line)
                            try:
                                if isinstance(document.get('_id'), dict):
                                    document['_id'] = document['_id']['$oid']
                                    success_count += 1
                                else:
                                    collection.insert_one(document)
                                    success_count += 1
                            except DuplicateKeyError:
                                duplicate_key_error += 1
                                continue
                            except Exception as e:
                                count += 1
                        print(f"\nℹ️  Log Details:---------------------\nDatabase : {folder}\nCollection : {collection_name}\nSuccess Count : {success_count} \nFail Count : {count}\nDuplicateKeyError : {get_duplicate_key_error_log(duplicate_key_error)}")
        except Exception as ex:
            print(f"Error:---------------------  {folder}\n {ex} \n\n")
    client.close()
    print("\n\n✅✅✅ Loading Process Done ✅✅✅")
else:
    print('🥺🥺🥺 There is no sample folders')
    print('🥺🥺🥺 Sample Dataloading Process Stopped')



